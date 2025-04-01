# Standard library
import logging
import os
import sys
import re
import subprocess
from openai import OpenAI
from pathlib import Path
from typing import Dict, Any, List, NoReturn

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
    Extracts all top-level function names from the given Python source code.

    This function uses a regular expression to find function definitions
    that start with `def` at the beginning of a line.

    Args:
        code (str): The Python source code to analyze.

    Returns:
        List[str]: A list of function names defined in the code.
    """
    return re.findall(r'^def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)

def extract_import_statements(code: str) -> List[str]:
    """
    Extracts all top-level import statements from the given Python source code.

    Matches both 'import module' and 'from module import name' statements
    that appear at the beginning of a line.

    Args:
        code (str): The Python source code to scan.

    Returns:
        List[str]: A list of import statements found in the code.
    """
    return re.findall(r'^(?:from\s+\S+\s+import\s+\S+|import\s+\S+)', code, re.MULTILINE)


def generate_test_prompt(prompt: str, file_content: str, file_path: str) -> str:
    """
    Formats a test generation prompt by injecting extracted import statements,
    function names, and metadata into a provided prompt template.

    Args:
        prompt (str): The prompt template with placeholders like {file_content}, {file_path},
                      {import_section}, and {import_hint}.
        file_content (str): The source code of the Python file.
        file_path (str): The path to the source file, used to construct import statements.

    Returns:
        str: A fully formatted prompt ready for use with an LLM.
    """
    function_names = extract_function_names(file_content)
    import_statements = extract_import_statements(file_content)

    module_path = file_path.replace("\\", "/").replace("/", ".").replace(".py", "")
    
    import_hint = (
        f"from {module_path} import {', '.join(function_names)}"
        if function_names else f"# No public functions found in {module_path}"
    )

    import_section = (
        "\n".join(import_statements) if import_statements else "# No imports found in original file"
    )
    print(f{import_section})
    return prompt.format(
        file_content=file_content,
        file_path=file_path,
        import_section=import_section,
        import_hint=import_hint,
    )


def _load_env_variables() -> Dict[str, Any]:
    """
    Loads required environment variables from a .env file and returns them
    as a dictionary.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing environment variable
        values for OpenAI API key, source directory, tests directory, and model name.
    """
    load_dotenv()  # Load environment variables from .env file

    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "src_dir": os.getenv("SRC_DIR"),
        "tests_dir": os.getenv("TESTS_DIR"),
        "model_name": os.getenv("MODEL_NAME"),
        "llm_test_prompt_template": os.getenv("LLM_TEST_PROMPT_TEMPLATE"),
    }

def generate_unit_tests(model_name: str, prompt: str, code: str, file_path: str) -> str:
    client = OpenAI()
    prompt = generate_test_prompt(prompt, code, file_path)
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


def save_test_file(src_dir: Path, test_dir: Path, original_path: Path, test_code: str) -> None:
    """
    Saves the generated test code to the appropriate location in the tests directory.

    Args:
        src_dir (Path): The root source directory.
        test_dir (Path): The root tests directory where test files are saved.
        original_path (Path): The path to the original source file.
        test_code (str): The generated test code as a string.
    """
    try:
        relative_path = original_path.relative_to(src_dir)
        test_path = test_dir / relative_path
        test_path = test_path.with_name(f"test_{test_path.name}")
        test_path.parent.mkdir(parents=True, exist_ok=True)
        test_path.write_text(test_code, encoding="utf-8")
    except Exception as e:
        print(f"❌ Failed to save test for {original_path}: {e}")

def clean_test_code(code: str) -> str:
    """
    Cleans LLM-generated test code by:
    - Removing code block fences (e.g., ```python)
    - Trimming to the last meaningful line (function, decorator, import, or class)
    - Normalizing line endings

    Args:
        code (str): The raw test code as generated by the LLM.

    Returns:
        str: The cleaned, ready-to-save test code.
    """
    lines = code.strip().splitlines()
    lines = [line for line in lines if not line.strip().startswith("```")]

    pattern = re.compile(r"^(def |@pytest|@patch|import |from |class )")
    last_code_index = max(
        (i for i, line in enumerate(lines) if pattern.match(line.strip())),
        default=len(lines) - 1
    )

    cleaned_lines = lines[:last_code_index + 1]
    return "\n".join(cleaned_lines).replace("\r", "")


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
    env_vars = _load_env_variables()

    
    
    if len(sys.argv) > 1:
        python_files = [Path(file) for file in sys.argv[1:] if file.endswith(file, ".py")]
    else:
        python_files = get_python_files(env_vars["src_dir"])

    for file_path in python_files:
        code = file_path.read_text(encoding="utf-8")
        if not code.strip():
            continue

        logger.info(f"🧠 Generating tests for {file_path}...")

        test_code = generate_unit_tests(
            model_name=env_vars["model_name"],
            prompt=env_vars["llm_test_prompt_template"],
            code=code,
            file_path=str(file_path)
        )
        save_test_file(
            Path(env_vars["src_dir"]),
            Path(env_vars["tests_dir"]),
            file_path,
            test_code
        )
        
        try:
            subprocess.run(["git", "add", env_vars["tests_dir"]], check=True)
            logger.info(f"✅ Staged test directory: {env_vars['tests_dir']}")
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to stage tests directory: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"❌ Unhandled error: {e}")
    finally:
        sys.exit(0)        
