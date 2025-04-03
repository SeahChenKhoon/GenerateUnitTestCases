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
    Extracts all top-level function names and public class method names
    from the given Python source code.

    This function finds:
      - Top-level functions (e.g., def func_name(...))
      - Public methods in classes (e.g., class X:\n    def method_name(...))

    Private/internal methods (starting with '_') are excluded.

    Args:
        code (str): The Python source code to analyze.

    Returns:
        List[str]: A list of public function and method names defined in the code.
    """
    function_names = set()

    # Extract top-level functions
    top_level_funcs = re.findall(r'^def\s+([a-zA-Z][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)
    function_names.update(top_level_funcs)

    # Extract class methods (public ones only)
    class_method_pattern = re.compile(
        r'^\s*class\s+\w+\s*:\s*(?:.|\n)*?'
        r'(?:(?<=\n)\s+def\s+([a-zA-Z][a-zA-Z0-9_]*)\s*\()',  # capture only public method names
        re.MULTILINE
    )
    class_methods = class_method_pattern.findall(code)
    function_names.update(class_methods)

    return sorted(function_names)

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
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "llm_provider": os.getenv("LLM_PROVIDER"),
        "src_dir": os.getenv("SRC_DIR"),
        "tests_dir": os.getenv("TESTS_DIR"),
        "model_name": os.getenv("MODEL_NAME"),
        "llm_test_prompt_template": os.getenv("LLM_TEST_PROMPT_TEMPLATE"),
    }


def generate_test_prompt(prompt: str, file_content: str, file_path: str, function_names:List[str]) -> tuple[str, str, str]:
    import_statements = extract_import_statements(file_content)

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

    # Log for debugging
    logger.info(f"import_hint : {import_hint}")
    logger.info(f"import_section : {import_section}")

    # Format the prompt using the provided template
    formatted_prompt = prompt.format(
        file_content=file_content,
        file_path=file_path,
        import_section=import_section,
        import_hint=import_hint,
    )

    return formatted_prompt, import_section, import_hint


def generate_unit_tests(model_arg, prompt: str, code: str, file_path: str, function_names:List[str]) -> str:
    client = OpenAI()


    # Prepare the full prompt and reuse import metadata
    formatted_prompt, import_section, import_hint = generate_test_prompt(prompt, code, file_path, function_names=function_names)

    # Generate test code from LLM
    response = client.chat.completions.create(
        model=model_arg,
        messages=[{"role": "user", "content": formatted_prompt}],
        temperature=0.2,
    )

    generated_test_code = response.choices[0].message.content.strip()

    # Ensure import_hint is present in output
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
    Cleans LLM-generated test code by:
    - Removing code block fences (e.g., ```python)
    - Trimming to the last meaningful line (function, decorator, import, or class)
    - Removing inline comments (everything after #)
    - Normalizing line endings

    Args:
        code (str): The raw test code as generated by the LLM.

    Returns:
        str: The cleaned, ready-to-save test code.
    """
    lines = code.strip().splitlines()

    # Remove markdown code fences
    lines = [line for line in lines if not line.strip().startswith("```")]

    # Remove inline comments (anything after '#')
    stripped_lines = []
    for line in lines:
        line_no_comment = line.split("#", 1)[0].rstrip()
        if line_no_comment:
            stripped_lines.append(line_no_comment)

    # Find last index of a line that starts a code block
    pattern = re.compile(r"^(def |@pytest|@patch|import |from |class )")
    last_code_index = None
    for i, line in enumerate(stripped_lines):
        if pattern.match(line.strip()):
            last_code_index = i

    # If found, include all lines after the last match to preserve multi-line blocks
    if last_code_index is not None:
        cleaned_lines = stripped_lines[last_code_index:]
    else:
        cleaned_lines = stripped_lines    
    return "\n".join(cleaned_lines).replace("\r", "")


def get_llm_client() -> Union[OpenAI, AzureOpenAI]:
    provider = os.getenv("LLM_PROVIDER").lower()

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
    

def main() -> NoReturn:
    """
    Main entry point for generating unit tests for Python files.

    This function:
    - Loads environment variables.
    - Identifies Python files to process:
        * If filenames are passed as command-line arguments (e.g., by pre-commit),
          only those files are processed.
        * Otherwise, all `.py` files in the configured `src_dir` are processed.
    - For each file:
        * Reads its content.
        * Generates pytest-style unit tests using an LLM.
        * Saves the generated tests to the corresponding location in `tests_dir`.
        * Stages the test files using `git add`.

    Raises:
        Logs an error if `git add` fails.
    """
    logger.info("Loading environment variables...")

    # Load required variables from .env or environment
    env_vars = _load_env_variables()
    model_arg  = get_llm_client()
    # Collect all Python source files from the configured source directory
    logger.info(f"env file: {env_vars["src_dir"]}")
    python_files = get_python_files(env_vars["src_dir"])

    # Iterate through each Python file and generate corresponding test cases
    for file_path in python_files:
        logger.info(f"Processing file: {file_path}")
        # Read the source code content from the file
        code = file_path.read_text(encoding="utf-8")

        # Skip files that are empty or contain only whitespace
        if not code.strip():
            continue

        logger.info(f"Generating tests for {file_path}...")
        # Clean the code to remove unnecessary parts
        code = clean_test_code(code)
        logger.info(f"cleaned code : {code}")

        # Extract function names and import lines from the file content
        function_names = extract_function_names(code)
        logger.info(f"function_names : {function_names}")

        if function_names:
            # Use LLM to generate test code based on the file's content and path
            test_code = generate_unit_tests(
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


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
    finally:
        sys.exit(0)        
