# Standard library
import logging
import os
import sys
import re
import ast
import subprocess
from openai import OpenAI, AzureOpenAI
from pathlib import Path
from typing import Dict, Any, List, NoReturn, Union

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

def get_python_files(directory: str) -> List[Path]:
    """
    Recursively retrieves all Python (.py) files within the given directory.

    Args:
        directory (str): The root directory to search for Python files.

    Returns:
        List[Path]: A list of Path objects representing all found .py files.
    """
    return list(Path(directory).rglob("*.py"))


def extract_function_names(code: str) -> List[str]:
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


def extract_import_statements(code: str) -> List[str]:
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
                imports.append(stmt)
    return imports


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
        "model_name": os.getenv("MODEL_NAME"),
        "llm_test_prompt_template": os.getenv("LLM_TEST_PROMPT_TEMPLATE"),
    }


def update_relative_imports(code: str, file_path: str) -> str:
    """
    Converts relative imports (e.g., from .. import x, from ..module import y) to absolute imports
    using only the file_path by treating its top-level directory as the root module.
    """
    file_path_obj = Path(file_path).with_suffix("")
    module_parts = list(file_path_obj.parts)
    
    # Match cases like:
    #   from . import models
    #   from .. import utils
    #   from ...llm_handler import OpenAI_llm
    #   from ..subpackage.module import something
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

def generate_test_prompt(prompt: str, file_content: str, file_path: str, function_names:List[str]) -> tuple[str, str, str]:
    logger.info(f"Hello World 10")
    import_statements = extract_import_statements(file_content)
    logger.info(f"Hello World 11")
    import_statements = update_relative_imports(code=file_content, file_path=file_path)
    logger.info(f"Hello World 12")

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
    logger.info(import_section)

    # Format the prompt using the provided template
    formatted_prompt = prompt.format(
        file_content=file_content,
        file_path=file_path,
        import_section=import_section,
        import_hint=import_hint,
    )

    return formatted_prompt, import_section, import_hint


def _get_model_arguments(provider: str, model_name: str = "", deployment_id: str = "") -> str:
    if provider.lower() == "azure":
        if not deployment_id:
            raise ValueError("deployment_id must be provided for Azure OpenAI")
        return deployment_id
    else:
        if not model_name:
            raise ValueError("model_name must be provided for OpenAI")
        return model_name
    

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


def generate_unit_tests(
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


def clean_test_code(code: str) -> str:
    """
    Removes inline comments (everything after '#') from a Python code string,
    while preserving docstrings and indentation.

    Args:
        code (str): Python source code as a string.

    Returns:
        str: Cleaned code with inline comments removed.
    """
    import io
    import tokenize

    cleaned_lines = []
    tokens = tokenize.generate_tokens(io.StringIO(code).readline)

    current_line = ""
    last_lineno = -1
    last_col = 0

    for token_type, token_string, (start_line, start_col), (_, end_col), line in tokens:
        if start_line != last_lineno:
            if current_line.strip():
                cleaned_lines.append(current_line.rstrip())
            current_line = ""
            last_col = 0
            last_lineno = start_line

        if token_type == tokenize.COMMENT:
            continue  # Skip comments
        if start_col > last_col:
            current_line += " " * (start_col - last_col)
        current_line += token_string
        last_col = end_col

    if current_line.strip():
        cleaned_lines.append(current_line.rstrip())

    return "\n".join(cleaned_lines)


def _get_llm_client(provider: str) -> Union[OpenAI, AzureOpenAI]:
    """
    Initializes and returns an OpenAI or AzureOpenAI client based on the provider.
    
    Args:
        provider (str): Either "openai" or "azure".

    Returns:
        Union[OpenAI, AzureOpenAI]: Configured API client.

    Raises:
        EnvironmentError: If required environment variables are missing.
        ValueError: If the provider is invalid.
    """
    provider = provider.lower()

    if provider == "azure":
        azure_key = os.getenv("AZURE_OPENAI_KEY")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        api_version = os.getenv("API_VERSION")

        if not azure_key or not azure_endpoint or not api_version:
            raise EnvironmentError(
                "Missing one or more Azure environment variables: "
                "AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, API_VERSION"
            )

        return AzureOpenAI(
            api_key=azure_key,
            api_version=api_version,
            azure_endpoint=azure_endpoint,
        )

    elif provider == "openai":
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            raise EnvironmentError("Missing required environment variable: OPENAI_API_KEY")

        return OpenAI(api_key=openai_key)

    else:
        raise ValueError(f"Unsupported provider: '{provider}'. Expected 'openai' or 'azure'.")
    
def is_special_python_file(file_path: str) -> bool:
    """
    Returns True if the file is a special Python file such as __init__.py or __main__.py.
    """
    special_files = {"__init__.py", "__main__.py", "__version__.py"}
    return Path(file_path).name in special_files


def main() -> NoReturn:
    logger.info("Loading environment variables...")
    processed_files = []

    # Load required variables from .env or environment
    env_vars = _load_env_variables()

    provider=env_vars["llm_provider"]
    client = _get_llm_client(provider=provider)
    model_arg = _get_model_arguments(provider=provider, model_name=env_vars["model_name"], deployment_id=env_vars["deployment_id"])

    # Collect all Python source files from the configured source directory
    logger.info(f"env file: {env_vars["src_dir"]}")
    python_files = get_python_files(env_vars["src_dir"])

    # Iterate through each Python file and generate corresponding test cases
    for file_path in python_files:
        logger.info(f"{BOLD}Start Processing file: {file_path}{RESET}")
        if is_special_python_file(str(file_path)):
            logger.info(f"{BOLD}End Processing file: {file_path} - is_special_python_file\n")
            continue

        # Read the source code content from the file
        code = file_path.read_text(encoding="utf-8")
        logger.info(f"Hello World 1")
        # Skip files that are empty or contain only whitespace
        if not code.strip():
            continue
        logger.info(f"Hello World 2")
        # Extract function names and import lines from the file content
        function_names = extract_function_names(code)
        logger.info(f"Hello World 3")
        logger.info(f"Generating tests for {file_path}...")
        if function_names:
            # Use LLM to generate test code based on the file's content and path
            logger.info(f"Hello World 4")
            test_code = generate_unit_tests(
                provider=client,
                model_arg=model_arg,
                prompt=env_vars["llm_test_prompt_template"],
                code=code,
                file_path=str(file_path),
                function_names=function_names
            )

            # Save the generated test to the tests directory
            test_path = save_test_file(
                Path(env_vars["src_dir"]),
                Path(env_vars["tests_dir"]),
                file_path,
                test_code
            )

        else:
            logger.warning(f"No public functions found in {file_path}. Skipping test generation.")

        try:
            # Optionally stage the tests directory (in case it's newly created)
            subprocess.run(["git", "add", env_vars["tests_dir"]], check=True)
            logger.info(f"Staged test directory: {env_vars['tests_dir']}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to stage tests directory: {e}")
        logger.info(f"{BOLD}End Processing file: {file_path}{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
    finally:
        sys.exit(0)        
