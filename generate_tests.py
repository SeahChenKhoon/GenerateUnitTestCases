# Standard library
import logging
import os
import sys
import re
import ast
import contextlib
import subprocess
import tempfile
from openai import OpenAI, AzureOpenAI
from pathlib import Path
from typing import Dict, Any, List, NoReturn, Union, Tuple

# Third-party packages
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

BOLD = "\033[1m"
RESET = "\033[0m"

def _initialize_llm(env_vars: dict) -> Tuple[Union[OpenAI, AzureOpenAI], str]:
    """
    Initializes the LLM client and retrieves the appropriate model argument based on the environment configuration.

    Args:
        env_vars (dict): A dictionary containing environment variables. Expected keys include:
            - "llm_provider": Either "openai" or "azure".
            - "model_name": (Required if provider is "openai") The OpenAI model name.
            - "deployment_id": (Required if provider is "azure") The Azure deployment ID.

    Returns:
        Tuple[Union[OpenAI, AzureOpenAI], str]: A tuple containing the initialized LLM client and
        the model argument (model name or deployment ID).

    Raises:
        EnvironmentError: If required environment variables are missing.
        ValueError: If an unsupported provider is specified or required model identifiers are missing.
    """
    provider = env_vars["llm_provider"]
    client = _get_llm_client(provider)
    model_arg = _get_model_arguments(
        provider=provider,
        model_name=env_vars.get("model_name", ""),
        deployment_id=env_vars.get("deployment_id", "")
    )
    return client, model_arg


def _process_file(file_path: Path, client: Union[OpenAI, AzureOpenAI], model_arg: str, env_vars: dict) -> None:
    """
    Processes a Python source file by extracting function names, generating unit tests using an LLM,
    and executing those tests.

    Args:
        file_path (Path): The path to the Python source file to be processed.
        client (Union[OpenAI, AzureOpenAI]): The initialized LLM client for generating test code.
        model_arg (str): The model name (for OpenAI) or deployment ID (for Azure OpenAI).
        env_vars (dict): A dictionary of environment variables, expected to contain:
            - "llm_test_prompt_template": The prompt template to guide test generation.

    Returns:
        None

    Logs:
        - Start and end of file processing.
        - Warnings if no public functions are found.
        - Errors if processing fails.
    """
    logger.info(f"{BOLD}Start Processing file: {file_path}{RESET}")

    try:
        code = file_path.read_text(encoding="utf-8")
        function_names = _extract_function_names(code)
        if not function_names:
            logger.warning(f"No public functions found in {file_path}. Skipping test generation.\n")
            return

        test_code = _generate_unit_tests(
            provider=client,
            model_arg=model_arg,
            prompt=env_vars["llm_test_prompt_template"],
            code=code,
            file_path=str(file_path),
            function_names=function_names
        )

        run_each_pytest_function_individually(test_code, env_vars["temp_dir"])
        
        if test_code:
            test_path = save_test_file(
                    Path(env_vars["src_dir"]),
                    Path(env_vars["tests_dir"]),
                    file_path,
                    test_code
                )

    except Exception as e:
        logger.error(f"Failed processing {file_path}: {e}")

    logger.info(f"{BOLD}End Processing file: {file_path}{RESET}\n")


def _stage_test_directory(tests_dir: str) -> None:
    """
    Stages the specified test directory using Git.

    Args:
        tests_dir (str): The path to the test directory to stage (e.g., via 'git add').

    Returns:
        None

    Logs:
        - Info message if staging is successful.
        - Error message if Git staging fails due to a subprocess error.
    """
    try:
        subprocess.run(["git", "add", tests_dir], check=True)
        logger.info(f"Staged test directory: {tests_dir}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to stage tests directory: {e}")


def _load_env_variables() -> Dict[str, Any]:
    """
    Loads required environment variables from a .env file and returns them
    as a dictionary.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing environment variable
        values for OpenAI API key, source directory, tests directory, and model name.
    """
    load_dotenv(override=True)  # Load environment variables from .env file

    return {
        "llm_provider": os.getenv("LLM_PROVIDER"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "azure_openai_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "azure_openai_key": os.getenv("AZURE_OPENAI_KEY"),
        "deployment_id": os.getenv("DEPLOYMENT_ID"),
        "api_version": os.getenv("API_VERSION"),        
        "src_dir": os.getenv("SRC_DIR"),
        "tests_dir": os.getenv("TESTS_DIR"),
        "temp_dir": os.getenv("TEMP_DIR"),
        "model_name": os.getenv("MODEL_NAME"),
        "llm_test_prompt_template": os.getenv("LLM_TEST_PROMPT_TEMPLATE"),
    }


def _get_llm_client(provider: str) -> Union[OpenAI, AzureOpenAI]:
    """
    Initializes and returns an LLM client (OpenAI or AzureOpenAI) based on the specified provider.

    Args:
        provider (str): The name of the LLM provider. Accepted values are "openai" or "azure".

    Returns:
        Union[OpenAI, AzureOpenAI]: An initialized client instance for the specified provider.

    Raises:
        EnvironmentError: If required environment variables for the selected provider are missing.
            - For "azure": AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, API_VERSION
            - For "openai": OPENAI_API_KEY
        ValueError: If the provider name is unsupported.
    """    
    provider = provider.lower()

    if provider == "azure":
        required_vars = {
            "AZURE_OPENAI_KEY": os.getenv("AZURE_OPENAI_KEY"),
            "AZURE_OPENAI_ENDPOINT": os.getenv("AZURE_OPENAI_ENDPOINT"),
            "API_VERSION": os.getenv("API_VERSION")
        }

        missing = [k for k, v in required_vars.items() if not v]
        if missing:
            raise EnvironmentError(f"Missing Azure environment variables: {', '.join(missing)}")

        return AzureOpenAI(
            api_key=required_vars["AZURE_OPENAI_KEY"],
            api_version=required_vars["API_VERSION"],
            azure_endpoint=required_vars["AZURE_OPENAI_ENDPOINT"],
        )

    if provider == "openai":
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            raise EnvironmentError("Missing required environment variable: OPENAI_API_KEY")
        return OpenAI(api_key=openai_key)

    raise ValueError(f"Unsupported provider: '{provider}'. Expected 'openai' or 'azure'.")


def _get_model_arguments(provider: str, model_name: str = "", deployment_id: str = "") -> str:
    """
    Returns the appropriate model argument based on the LLM provider.

    Args:
        provider (str): The name of the LLM provider. Accepted values are "openai" or "azure".
        model_name (str, optional): The model name to use for OpenAI. Required if provider is "openai".
        deployment_id (str, optional): The deployment ID to use for Azure OpenAI. Required if provider is "azure".

    Returns:
        str: The selected model argument (either the model name or deployment ID).

    Raises:
        ValueError: If the required argument for the given provider is missing,
                    or if the provider is unsupported.
    """
    provider = provider.lower()

    if provider == "azure":
        if not deployment_id:
            raise ValueError("deployment_id must be provided for Azure OpenAI")
        return deployment_id

    if provider == "openai":
        if not model_name:
            raise ValueError("model_name must be provided for OpenAI")
        return model_name

    raise ValueError(f"Unsupported provider: '{provider}'.")


def _get_python_files(directory: str) -> List[Path]:
    """
    Recursively retrieves all Python (.py) files within the given directory.

    Args:
        directory (str): The root directory to search for Python files.

    Returns:
        List[Path]: A list of Path objects representing all found .py files.
    """
    return list(Path(directory).rglob("*.py"))


def _extract_function_names(code: str) -> List[str]:
    """
    Extracts all top-level function and class names from the given Python source code.

    This includes both `def` and `async def` functions, and class definitions.

    Args:
        code (str): The Python source code to analyze.

    Returns:
        List[str]: A list of function and class names defined in the code.
    """
    function_names = re.findall(r'^(?:async\s+)?def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)
    class_names = re.findall(r'^class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)
    return sorted(set(function_names + class_names))


def update_relative_imports(code: str, file_path: str) -> str:
    """
    Converts relative import statements in Python code to absolute imports based on the file path.

    This function detects imports like:
        - from . import module
        - from ..subpackage import something
        - from ... import x

    And rewrites them as absolute imports using the structure of the provided file path.

    Args:
        code (str): The Python source code containing relative import statements.
        file_path (str): The full path to the Python file (e.g., 'project/module/file.py').

    Returns:
        str: The updated source code with relative imports converted to absolute imports.

    Raises:
        ValueError: If the number of relative import levels (e.g., '..', '...') exceeds
                    the depth of the file path.
    """
    file_path_obj = Path(file_path).with_suffix("")
    module_parts = list(file_path_obj.parts)
    pattern = re.compile(r"from\s+(\.+)([\w\.]*)\s+import\s+(\w+)")

    def replacer(match):
        dots = match.group(1)                  # ., .., ...
        relative_module = match.group(2)       # can be empty or nested (e.g., llm_handler or sub.module)
        imported_name = match.group(3)         # imported object

        levels_up = len(dots)
        if levels_up > len(module_parts):
            raise ValueError(f"Too many dots in relative import for path {file_path}")

        # Trim path upward based on levels
        base_parts = module_parts[:len(module_parts) - levels_up]
        # Append relative module parts (if any)
        if relative_module:
            base_parts.extend(relative_module.split("."))

        absolute_import = ".".join(base_parts)
        return f"from {absolute_import} import {imported_name}"

    return pattern.sub(replacer, code)


def extract_import_statements(code: str, file_path:str) -> List[str]:
    """
    Extracts and returns all import statements from the given Python source code,
    with relative imports converted to absolute imports based on the file path.

    Args:
        code (str): The Python source code as a string.
        file_path (str): The path to the Python file from which the code was extracted.

    Returns:
        List[str]: A list of formatted import statements, with relative imports updated
        to absolute paths using `update_relative_imports`.

    Notes:
        - If the code contains a syntax error, an empty list is returned.
        - Only top-level and nested `import` or `from ... import ...` statements are extracted.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []  # or handle parsing errors if needed
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            # Get the exact source text for the import node
            stmt = ast.get_source_segment(code, node)
            if stmt is not None:
                imports.append(update_relative_imports(stmt,file_path))
    return imports


def generate_test_prompt(prompt: str, file_content: str, file_path: str, function_names:List[str]) -> tuple[str, str, str]:
    """
    Generates a formatted test generation prompt for an LLM based on the given file content and metadata.

    Args:
        prompt (str): A template string containing placeholders for file content, path, and imports.
        file_content (str): The raw Python source code of the file to be tested.
        file_path (str): The path to the source file (used for import resolution).
        function_names (List[str]): A list of public function names extracted from the source code.

    Returns:
        tuple[str, str, str]: A tuple containing:
            - formatted_prompt: The final prompt string filled with relevant context.
            - import_section: The constructed import section with `import pytest` and resolved imports.
            - import_hint: A suggested import line for the test file based on function names and module path.

    Notes:
        - Relative imports in the file are converted to absolute ones using `extract_import_statements`.
        - The function constructs a clean import section for inclusion in generated test code.
        - If no public functions are found, a comment is inserted instead of an import hint.
    """
    import_statements = extract_import_statements(file_content, file_path)

    # Convert file path to module path (dot-separated)
    module_path = file_path.replace("\\", "/").replace("/", ".").replace(".py", "")

    # Create import hint for testing public functions
    import_hint = (
        f"from {module_path} import {', '.join(function_names)}"
        if function_names else f"# No public functions found in {module_path}"
    )

    # Prepend "import pytest" to the original file's imports
    import_section = (
        "import pytest\n" + "\n".join(import_statements)
        if import_statements else "import pytest\n# No imports found in original file"
    )
    # logger.info(import_section)

    # Format the prompt using the provided template
    formatted_prompt = prompt.format(
        file_content=file_content,
        file_path=file_path,
        import_section=import_section,
        import_hint=import_hint,
    )

    return formatted_prompt, import_section, import_hint


def strip_markdown_fences(text: str) -> str:
    """
    Removes Markdown-style triple backtick fences from LLM output.
    Logs a warning if any stripping was performed.

    Args:
        text (str): The raw LLM output string.

    Returns:
        str: The cleaned string without Markdown-style code fences.
    """
    lines = text.strip().splitlines()
    modified = False

    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
        modified = True

    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]
        modified = True

    if modified:
        logger.warning("Stripped Markdown-style triple backtick fences from LLM output.")

    return "\n".join(lines)


def _generate_unit_tests(
    provider: Union[OpenAI, AzureOpenAI],
    model_arg: str,
    prompt: str,
    code: str,
    file_path: str,
    function_names: List[str]
) -> str:
    """
    Generates pytest-style unit test code using an LLM (OpenAI or Azure OpenAI).

    Args:
        provider (Union[OpenAI, AzureOpenAI]): An initialized LLM client.
        model_arg (str): Model name (for OpenAI) or deployment ID (for Azure OpenAI).
        prompt (str): The base instruction to guide the test generation.
        code (str): The source code to be tested.
        file_path (str): The path of the source file.
        function_names (List[str]): A list of function names to generate tests for.

    Returns:
        str: Generated unit test code as a string.
    """
    formatted_prompt, import_section, import_hint = generate_test_prompt(
        prompt=prompt, file_content=code, file_path=file_path, function_names=function_names
    )

    response = provider.chat.completions.create(
        model=model_arg,
        messages=[{"role": "user", "content": formatted_prompt}],
        temperature=0.2,
    )

    generated_test_code = strip_markdown_fences(response.choices[0].message.content.strip())

    if import_hint not in generated_test_code:
        logger.warning("Import_hint missing from generated output. Injecting it manually.")
        generated_test_code = f"{import_section}\n{import_hint}\n\n{generated_test_code}"
    return generated_test_code


def extract_test_functions(code: str) -> List[str]:
    """
    Extracts all top-level test function names from the given test code string.
    """
    return re.findall(r'^def\s+(test_\w+)\s*\(', code, re.MULTILINE)

def save_test_file(src_dir: Path, test_dir: Path, original_path: Path, test_code: str) -> Path:
    """
    Saves the generated test code to the appropriate location in the tests directory.

    Args:
        src_dir (Path): The root source directory.
        test_dir (Path): The root tests directory where test files are saved.
        original_path (Path): The path to the original source file.
        test_code (str): The generated test code as a string.

    Returns:
        Path: The path to the saved test file.
    """
    relative_path = original_path.relative_to(src_dir)
    test_path = test_dir / relative_path
    test_path = test_path.with_name(f"test_{test_path.name}")
    test_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.write_text(test_code, encoding="utf-8")
    return test_path


def run_each_pytest_function_individually(test_code: str, temp_path: Path) -> str:
    results = []

    # Extract all import statements
    import_lines = "\n".join(re.findall(r"^(import .+|from .+ import .+)", test_code, re.MULTILINE))

    # Extract each test function body individually
    test_functions = re.findall(
        r"(def\s+test_[\w_]+\s*\([^)]*\):(?:\n(?: {4}|\t).+)+)", test_code
    )

    all_test_code = import_lines +"\n"

    for test_func_code in test_functions:
        # Extract test function name
        match = re.match(r"def\s+(test_[\w_]+)", test_func_code)
        if not match:
            continue
        test_name = match.group(1)

        # Compose full temp test code (imports + 1 test)
        full_test_code = f"{import_lines}\n\n{test_func_code}\n"
        # Save to temp file
        temp_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path.write_text(full_test_code, encoding="utf-8")

        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(".").resolve()) 
        # Run pytest on that file and function
        result = subprocess.run(
            ["pytest", str(temp_path), "-k", test_name, "--tb=short", "--quiet"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env
        )

        passed = result.returncode == 0
        if passed:
            all_test_code += "\n" + test_func_code + "\n"
        else:
            logger.info("Not all test case passed")
    return all_test_code



def main() -> NoReturn:
    logger.info("Loading environment variables...")

    try:
        env_vars = _load_env_variables()
        client, model_arg = _initialize_llm(env_vars)
        python_files = _get_python_files(env_vars["src_dir"])
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        raise

    for file_path in python_files:
        output = _process_file(file_path, client, model_arg, env_vars)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
    finally:
        sys.exit(0)        
