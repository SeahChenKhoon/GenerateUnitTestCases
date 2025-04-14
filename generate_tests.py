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
        "final_dir": os.getenv("FINAL_DIR"),        
        "temp_file": os.getenv("TEMP_FILE"),
        "model_name": os.getenv("MODEL_NAME"),
        "llm_test_prompt": os.getenv("LLM_TEST_PROMPT"),
        "temperature": os.getenv("TEMPERATURE"),
        "llm_import_prompt": os.getenv("LLM_IMPORT_PROMPT"),
        "llm_new_import_prompt": os.getenv("LLM_NEW_IMPORT_PROMPT"),
        "llm_resolve_prompt": os.getenv("LLM_RESOLVE_PROMPT")
        
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


def extract_function_and_class_names(code: str):
    # Match def and async def at any indentation level (including top-level)
    function_names = re.findall(r'^\s*(?:async\s+)?def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)

    # Match class definitions at any indentation level
    class_names = re.findall(r'^\s*class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)

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


def generate_test_prompt(llm_test_prompt: str, import_statements: str, file_content: str, source_code_path: str, function_names:List[str]) -> tuple[str, str, str]:
    formatted_prompt = llm_test_prompt.format(
        file_content=file_content,
        file_path=source_code_path,
        import_statements=import_statements,
    )

    return formatted_prompt, import_statements


def strip_markdown_fences(text: str) -> str:
    """
    Removes all Markdown-style triple backtick fences from LLM output.
    Logs a warning if any stripping was performed.

    Args:
        text (str): The raw LLM output string.

    Returns:
        str: The cleaned string without Markdown-style code fences.
    """
    lines = text.strip().splitlines()
    cleaned_lines = []
    modified = False

    for line in lines:
        if line.strip().startswith("```"):
            modified = True
            continue  # Skip the fence line
        cleaned_lines.append(line)

    if modified:
        logger.warning("Stripped Markdown-style triple backtick fences from LLM output.")

    return "\n".join(cleaned_lines)

def get_chat_completion(provider: Any, model: str, prompt: str, temperature: float = 0.2) -> Any:
    """
    Sends a prompt to the chat model and returns the response.

    Args:
        provider (Any): The provider instance with a chat.completions.create method.
        model (str): The model name to use.
        prompt (str): The user prompt to send.
        temperature (float, optional): Sampling temperature. Defaults to 0.2.

    Returns:
        Any: The response object from the provider.
    """
    return provider.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

def identify_new_import(provider, model_arg, llm_new_import_prompt, test_case, import_statement, temperature):
        # Format the prompt using the provided template
    formatted_prompt = llm_new_import_prompt.format(
        test_case=test_case,
        import_statement=import_statement
    )
    
    response = get_chat_completion(provider, model_arg, formatted_prompt, temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())

def generate_import_statement(function_names: List[str], source_code_path: str) -> str:
    """
    Generates a Python import statement for the given function/class names from a source file path.

    Args:
        function_names (List[str]): A list of function or class names to import.
        source_code_path (str): Path to the source file, e.g., 'theory_evaluation/models.py'.

    Returns:
        str: A valid Python import statement.
    """
    # Remove .py extension and replace slashes with dots
    module_path = source_code_path.replace("/", ".").replace("\\", ".")
    if module_path.endswith(".py"):
        module_path = module_path[:-3]

    imports = ", ".join(function_names)
    return f"from {module_path} import {imports}"


def _generate_unit_tests(
    provider: Union[OpenAI, AzureOpenAI],
    model_arg: str,
    llm_test_prompt: str,
    llm_import_prompt: str, 
    temperature: float,
    function_names: List[str],
    source_code: str,
    source_code_path: str
) -> str:
    
    import_statements = extract_unique_imports(provider, model_arg, llm_import_prompt, source_code, temperature)
    import_statements = update_relative_imports(import_statements, source_code_path)
    import_statements += "\n" + generate_import_statement(function_names, source_code_path)

    formatted_prompt = llm_test_prompt.format(
        file_content=source_code,
        file_path=source_code_path,
        import_statements=import_statements,
    )

    response = get_chat_completion(provider, model_arg, formatted_prompt, temperature)
    generated_test_code = strip_markdown_fences(response.choices[0].message.content.strip())
    return generated_test_code, import_statements


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


def extract_test_cases_from_code(test_code: str) -> List[str]:
    """
    Extracts each full test case (with decorators and body) from a test file's code.

    A test case is defined as any top-level function whose name starts with `test_`,
    optionally preceded by one or more decorators.

    Args:
        test_code (str): The raw test file source code.

    Returns:
        List[str]: A list of full test function blocks as strings.
    """
    pattern = re.compile(
        r"""
        (                                   # Capture the entire function + decorators
            (?:@[\w\.]+\s*(?:\([^\n]*\))?\n)*  # Optional decorators
            def\s+test_[\w_]+\s*\(.*?\):       # The function signature
            (?:\n(?:[ \t]+.+))+                # The indented body lines
        )
        """,
        re.VERBOSE | re.MULTILINE
    )
    return pattern.findall(test_code)


def save_test_case_to_temp_file(import_lines: str, test_func: str, temp_path: Path) -> None:
    """
    Combines import statements and a test function into one file and writes it to the given path.

    Args:
        import_lines (str): The import statements to include.
        test_func (str): The test function code.
        temp_path (Path): The full file path where the test code should be saved.
    """
    full_test_code = f"{import_lines}\n\n{test_func}\n"
    temp_path.write_text(full_test_code, encoding="utf-8")

def run_single_test_file(temp_path: Path) -> Tuple[bool, str]:
    """
    Runs pytest on a file that contains a single test function.

    Args:
        temp_path (Path): Path to the test file.

    Returns:
        Tuple[bool, str]: (test_passed, test_output)
    """
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(".").resolve())

    result = subprocess.run(
        ["pytest", str(temp_path), "--tb=short", "--quiet"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env
    )
    passed = result.returncode == 0
    return passed, result.stdout.strip()

def extract_unique_imports(provider, model_arg, llm_get_import_prompt, test_code, temperature):
        # Format the prompt using the provided template
    formatted_prompt = llm_get_import_prompt.format(
        python_code=test_code
    )
    
    response = get_chat_completion(provider, model_arg, formatted_prompt, temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())


def resolve_unit_test(provider, model_arg, llm_resolve_prompt, test_case, test_case_error, temperature):
    # Format the prompt using the provided template
    formatted_prompt = llm_resolve_prompt.format(
        test_case=test_case,
        test_case_error=test_case_error
    )
    logger.info(f"formatted_prompt - {formatted_prompt}")
    response = get_chat_completion(provider, model_arg, formatted_prompt, temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())


from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def run_each_pytest_function_individually(
    provider,
    model_arg,
    temperature,
    llm_resolve_prompt,
    import_statements,
    source_code: str,
    test_code: str,
    temp_file: Path
) -> str:
    # Extract each test function body individually
    test_cases = extract_test_cases_from_code(test_code)
    success_test_cases = ""
    for idx, test_case in enumerate(test_cases, start=1):
        passed = 0
        count = 0
        logger.info(f"\n")
        logger.info(f"TEST CASE {idx} Retry {count + 1}")
        logger.info(f"---------------")
        logger.info(f"{test_case}")
        logger.info(f"---------------")
        try:
            save_test_case_to_temp_file(import_statements, test_case, temp_file)
            passed, test_case_error = run_single_test_file(temp_file)

            logger.info(f"passed {count + 1}- {passed}")
            logger.info(f"test_case_error {count + 1} - {test_case_error}")

            max_retries = 2
            while count < max_retries and not passed:
                count += 1
                logger.info(f"TEST CASE {idx} Retry {count + 1}")
                logger.info(f"---------------")
                logger.info(f"{test_case}")
                logger.info(f"---------------")
                missing_import_statement = resolve_unit_test(
                    provider, model_arg, llm_resolve_prompt, test_case, test_case_error, temperature
                )
                logger.info(f"missing_import_statement {count + 1}- {missing_import_statement}")

                if missing_import_statement:
                    import_statements += "\n" + missing_import_statement + "\n"
                    logger.info(f"new import statement {count + 1}- {import_statements}")
                    save_test_case_to_temp_file(import_statements, test_case, temp_file)
                    passed, test_case_error = run_single_test_file(temp_file)

                    if passed:
                        logger.info(f"passed {count + 1}- {passed}")
                        logger.info(f"test_case_error {count + 1} - {test_case_error}")

                else:
                    logger.info("Error due to unit test case fault")

            if passed:
                success_test_cases += "\n" + test_case + "\n"
            else:
                logger.info(f"Failed after all retries for test case {idx}")

        except Exception as e:
            logger.exception(f"Exception occurred while processing test case {idx}: {e}")

    return import_statements + "\n" + success_test_cases


def _process_file(source_code_path: Path, client: Union[OpenAI, AzureOpenAI], model_arg: str, env_vars: dict) -> None:
    logger.info(f"{BOLD}Start Processing file: {source_code_path}{RESET}")

    try:
        source_code = source_code_path.read_text(encoding="utf-8")
        function_names = extract_function_and_class_names(source_code)
        if not function_names:
            logger.warning(f"No public functions found in {source_code_path}. Skipping test generation.\n")
            return
        temperature=float(env_vars["temperature"])
        test_code, import_statements = _generate_unit_tests(
            provider=client,
            model_arg=model_arg,
            llm_test_prompt=env_vars["llm_test_prompt"],
            llm_import_prompt=env_vars["llm_import_prompt"],
            temperature=temperature,
            function_names=function_names,
            source_code=source_code,
            source_code_path=str(source_code_path)
        )

        if test_code:
            save_test_file(
                    Path(env_vars["src_dir"]),
                    Path(env_vars["tests_dir"]),
                    source_code_path,
                    test_code
                )

            test_code = run_each_pytest_function_individually(client, model_arg, temperature, env_vars["llm_resolve_prompt"], import_statements, source_code, test_code, Path(env_vars["temp_file"]))
        
            if test_code:
                save_test_file(
                        Path(env_vars["src_dir"]),
                        Path(env_vars["final_dir"]),
                        source_code_path,
                        test_code
                    )

    except Exception as e:
        logger.error(f"Failed processing {source_code_path}: {e}")

    logger.info(f"{BOLD}End Processing file: {source_code_path}{RESET}\n")


def main() -> NoReturn:
    logger.info("Loading environment variables...")

    try:
        env_vars = _load_env_variables()
        client, model_arg = _initialize_llm(env_vars)
        source_code_files = _get_python_files(env_vars["src_dir"])
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        raise

    for source_code_path in source_code_files:
        output = _process_file(source_code_path, client, model_arg, env_vars)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
    finally:
        sys.exit(0)        
