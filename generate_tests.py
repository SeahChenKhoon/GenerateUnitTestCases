# Standard library
import logging
import os
import sys
import re
import ast
import subprocess
from tabulate import tabulate
import pandas as pd 
from openai import OpenAI, AzureOpenAI
from pathlib import Path
from typing import Dict, Any, List, NoReturn, Union, Tuple

# Third-party packages
from dotenv import load_dotenv
os.makedirs("logs", exist_ok=True)
# Create file handler
file_handler = logging.FileHandler("logs/output.log")  # Make sure "logs/" exists or change path
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Configure logging accordingly
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Remove any existing handlers (especially default StreamHandler from basicConfig)
if logger.hasHandlers():
    logger.handlers.clear()

# Add the file handler
logger.addHandler(file_handler)


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
        azure_deployment_id=env_vars.get("azure_deployment_id", "")
    )
    return client, model_arg


def _load_env_variables() -> Dict[str, Any]:
    load_dotenv(override=True)  # Load environment variables from .env file
    return {
        "llm_provider": os.getenv("LLM_PROVIDER"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "azure_openai_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "azure_openai_key": os.getenv("AZURE_OPENAI_KEY"),
        "azure_deployment_id": os.getenv("AZURE_DEPLOYMENT_ID"),
        "azure_api_version": os.getenv("AZURE_API_VERSION"),        
        "source_dir": os.getenv("SOURCE_DIR"),
        "generated_tests_dir": os.getenv("GENERATED_TESTS_DIR"),
        "finalized_tests_dir": os.getenv("FINALIZED_TESTS_DIR"),
        "temp_test_file": os.getenv("TEMP_TEST_FILE"),
        "failed_tests_dir": os.getenv("FAILED_TESTS_DIR"),
        "model_name": os.getenv("MODEL_NAME"),
        "python_version": os.getenv("PYTHON_VERSION"),
        "llm_temperature": os.getenv("LLM_TEMPERATURE"),
        "llm_test_prompt": os.getenv("LLM_TEST_PROMPT"),
        "llm_import_prompt": os.getenv("LLM_IMPORT_PROMPT"),
        "llm_unique_import_prompt": os.getenv("LLM_UNIQUE_IMPORT_PROMPT"),
        "llm_resolve_prompt": os.getenv("LLM_RESOLVE_PROMPT"),
        "llm_pytest_fixture_prompt": os.getenv("LLM_PYTEST_FIXTURE_PROMPT"),
        "llm_test_cases_prompt": os.getenv("LLM_TEST_CASES_PROMPT"),
        "llm_cleanup_prompt": os.getenv("LLM_CLEANUP_PROMPT"),
        "requirements_txt": Path("./requirements.txt").read_text(encoding="utf-8")
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


def _get_model_arguments(provider: str, model_name: str = "", azure_deployment_id: str = "") -> str:
    provider = provider.lower()

    if provider == "azure":
        if not azure_deployment_id:
            raise ValueError("azure_deployment_id must be provided for Azure OpenAI")
        return azure_deployment_id

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


def extract_function_class_and_factory_assignments(code: str) -> List[str]:
    # Match top-level (not indented) functions
    function_names = re.findall(
        r'^(?:async\s+)?def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE
    )

    # Match class names
    class_names = re.findall(
        r'^class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*[:\(]', code, re.MULTILINE
    )

    factory_assignments = re.findall(
        r'^([A-Z][a-zA-Z0-9_]*)\s*=\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\(', code, re.MULTILINE
    )

    return sorted(set(function_names + class_names + factory_assignments))

def update_relative_imports(code: str, file_path: str) -> str:
    logger.info(f"Update relative import start")
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
    logger.info(f"Update relative import complete")
    return pattern.sub(replacer, code)


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

def get_chat_completion(provider: Any, model: str, prompt: str, llm_temperature: float = 0.2) -> Any:
    """
    Sends a prompt to the chat model and returns the response.

    Args:
        provider (Any): The provider instance with a chat.completions.create method.
        model (str): The model name to use.
        prompt (str): The user prompt to send.
        llm_temperature (float, optional): Sampling llm_temperature. Defaults to 0.2.

    Returns:
        Any: The response object from the provider.
    """
    return provider.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=llm_temperature,
    )


def generate_import_statement(function_names: list[str], source_code_path: str) -> str:
    # Convert file path to module path (e.g., theory_evaluation/llm_handler.py → theory_evaluation.llm_handler)
    module_path = os.path.splitext(source_code_path.replace(os.sep, "."))[0]

    # Join the function/class names
    names_str = ", ".join(function_names)

    return f"from {module_path} import {names_str}"


def _generate_unit_tests(
    provider: Union[OpenAI, AzureOpenAI],
    model_arg: str,
    llm_test_prompt: str,
    llm_import_prompt: str,
    requirements_txt:str,
    python_version:str,
    llm_temperature: float,
    function_names: List[str],
    source_code: str,
    source_code_path: str
) -> str:
    logger.info(f"Generate Unit Test Case starts")
    import_statements = extract_unique_imports(provider, model_arg, llm_import_prompt, source_code, llm_temperature)
    import_statements = update_relative_imports(import_statements, source_code_path)
    import_statements += "\n" + generate_import_statement(function_names, source_code_path)

    formatted_prompt = llm_test_prompt.format(
        file_content=source_code,
        file_path=source_code_path,
        import_statements=import_statements,
        requirements_txt=requirements_txt,
        python_version=python_version

    )

    response = get_chat_completion(provider, model_arg, formatted_prompt, llm_temperature)
    generated_test_code = strip_markdown_fences(response.choices[0].message.content.strip())
    return generated_test_code, import_statements


def save_test_file(source_dir: Path, test_dir: Path, original_path: Path, test_code: str) -> Path:
    relative_path = original_path.relative_to(source_dir)
    test_path = test_dir / relative_path
    test_path = test_path.with_name(f"test_{test_path.name}")
    test_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.write_text(test_code, encoding="utf-8")
    return test_path


def extract_test_cases_from_code(provider, model_arg, llm_test_cases_prompt, test_code, 
                    llm_temperature):
    
    formatted_prompt = llm_test_cases_prompt.format(
        unit_test_file=test_code
    )
    response = get_chat_completion(provider, model_arg, formatted_prompt, llm_temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())

def extract_test_functions(code: str) -> List[str]:
    """
    Extracts all test functions (including decorators like @pytest.mark.asyncio)
    from the provided Python source code and returns them as a list of strings.
    """
    # Pattern to match each @pytest.mark.asyncio async def test_xxx(...) with its full body
    pattern = re.compile(
        r'(@pytest\.mark\.asyncio\s*\n)?'                      # Optional @pytest.mark.asyncio
        r'(?:async\s+)?def\s+test_[\w_]+\s*\([^)]*\):'  # Function definition
        r'(?:\n(?: {4}|\t).+)+',                               # Indented function body
        re.MULTILINE
    )

    return [match.group().strip() for match in pattern.finditer(code)]

def save_test_case_to_temp_file(full_test_code: str, temp_path: Path) -> None:
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

def extract_unique_imports(provider, model_arg, llm_get_import_prompt, test_code, llm_temperature):
    # Format the prompt using the provided template
    logger.info(f"Extract unique import start")
    formatted_prompt = llm_get_import_prompt.format(
        python_code=test_code
    )
    
    response = get_chat_completion(provider, model_arg, formatted_prompt, llm_temperature)
    logger.info(f"Extract unique import complete")
    return strip_markdown_fences(response.choices[0].message.content.strip())


def resolve_unit_test(provider, model_arg, llm_resolve_prompt, test_case, test_case_error, source_code, requirements_txt, llm_temperature):
    formatted_prompt = llm_resolve_prompt.format(
        test_case=test_case,
        test_case_error=test_case_error,
        requirements_txt=requirements_txt,
        source_code=source_code
    )
    response = get_chat_completion(provider, model_arg, formatted_prompt, llm_temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())

def generate_improved_test_case(provider, model_arg, llm_cleanup_prompt, success_test_cases, llm_temperature): 
    # Format the prompt using the provided template
    formatted_prompt = llm_cleanup_prompt.format(
        test_code={success_test_cases}
    )
    response = get_chat_completion(provider, model_arg, formatted_prompt, llm_temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())

from pathlib import Path
import logging

logger = logging.getLogger(__name__)

    
def extract_pytest_fixture(provider, model_arg, llm_pytest_fixture_prompt, test_code, 
                    llm_temperature):
    formatted_prompt = llm_pytest_fixture_prompt.format(
        unit_test_file=test_code
    )
    response = get_chat_completion(provider, model_arg, formatted_prompt, llm_temperature)
    return strip_markdown_fences(response.choices[0].message.content.strip())
    
def run_each_pytest_function_individually(
    provider,
    model_arg,
    llm_temperature,
    python_version,
    requirements_txt,
    llm_resolve_prompt,
    llm_new_import_prompt, 
    llm_pytest_fixture_prompt,
    llm_test_cases_prompt,
    llm_cleanup_prompt, 
    import_statements,
    source_code: str,
    test_code: str,
    temp_test_file: Path
):
    logger.info(f"run_each_pytest_function_individually start")
    initial_template = ""
    passed_count = 0
    
    # Extract each test function body individually
    pytest_fixture = extract_pytest_fixture(provider, model_arg, llm_pytest_fixture_prompt, test_code, llm_temperature)
    test_cases_str = extract_test_cases_from_code(provider, model_arg, llm_test_cases_prompt, test_code, llm_temperature)
    test_cases = extract_test_functions(test_cases_str)

    total_test_case = len(test_cases)
    logger.info(f"Number of test case to process - {total_test_case}")

    if "pytest" in test_code and "import pytest" not in import_statements:
        import_statements += "\nimport pytest"
        logger.info(f"Import pytest manually.")

    if "patch" in test_code and "import patch" not in import_statements:
        import_statements += "\nfrom unittest.mock import patch"
        logger.info(f"Import patch manually.")

    if "mock_open" in test_code and "import mock_open" not in import_statements:
        import_statements += "\nfrom unittest.mock import mock_open"
        logger.info(f"Import mock_open manually.")

    success_test_cases = f"{import_statements}\n\n{pytest_fixture}"
    test_file_failure= f""

    for idx, test_case in enumerate(test_cases, start=1):
        passed = 0
        retry_count = 0
        max_retries = 3
        unit_test_failure = ""
        initial_template = f"{import_statements}\n{pytest_fixture}"
        try:
            while retry_count < max_retries and not passed:
                formatted_test_case_output=f"\nStart Processing TEST CASE {idx} Retry {retry_count}"
                logger.info(formatted_test_case_output)
                
                full_test_code = f"{initial_template}\n{test_case}\n"
                logger.info(f"Hello World - before full_test_code \n{full_test_code}")
                full_test_code = generate_improved_test_case(provider, model_arg, llm_cleanup_prompt, full_test_code, llm_temperature)
                logger.info(f"Hello World - after full_test_code \n{full_test_code}")
                formatted_test_case_output=f"\nTEST CASE {idx} Retry {retry_count}\n---------------\n{full_test_code}\n---------------"
                
                save_test_case_to_temp_file(full_test_code, temp_test_file)
                passed, test_case_error = run_single_test_file(temp_test_file)
                formatted_test_result=f"TEST CASE {idx} Retry {retry_count} - Result - {'Passed\n' if passed == 1 else 'Failed'}"
                logger.info(formatted_test_result)
                if passed:
                    unit_test_failure=""
                    passed_count += 1
                else:
                    test_case_error_message=f"Test Error -\n{test_case_error}\n" 
                    logger.info(test_case_error_message)
                    unit_test_failure += f"{formatted_test_case_output}\n{full_test_code}\n{formatted_test_result}\n{test_case_error_message}"
                    test_case = resolve_unit_test(provider, model_arg, llm_resolve_prompt, test_case, test_case_error, source_code, requirements_txt, llm_temperature)
                retry_count += 1
            if passed:
                success_test_cases += "\n" + test_case + "\n"
            else:
                test_file_failure+=unit_test_failure + "\n"
                logger.info(f"Failed after all retries for test case {idx}")
                logger.info(f"test_file_failure {test_file_failure}")

        except Exception as e:
            logger.exception(f"Exception occurred while processing test case {idx}: {e}")

    success_test_cases = initial_template + "\n" + success_test_cases
    improved_test_case = generate_improved_test_case(provider, model_arg, llm_cleanup_prompt, success_test_cases, llm_temperature)
    save_test_case_to_temp_file(improved_test_case, temp_test_file)
    passed, test_case_error = run_single_test_file(temp_test_file)
    if passed:
        logger.info(f"Improvement of test cases processed successfully")
        return_test_cases = improved_test_case
    else:
        return_test_cases = success_test_cases
        logger.info(f"Error in generating improved test cases\nTest case:\n{improved_test_case}\nTest error:\n{test_case_error}")

    logger.info(f"run_each_pytest_function_individually complete")
    return return_test_cases, test_file_failure, total_test_case, passed_count


def _process_file(source_code_path: Path, client: Union[OpenAI, AzureOpenAI], model_arg: str, env_vars: dict) -> None:
    logger.info(f"\nStart Processing file: {source_code_path}")

    try:
        source_code = source_code_path.read_text(encoding="utf-8")
        logger.info(f"Extraction of function and class start")
        function_names = extract_function_class_and_factory_assignments(source_code)
        logger.info(f"extraction of function and class complete")
        if not function_names:
            logger.warning(f"No public functions found in {source_code_path}. Skipping test generation.\n")
            return
        llm_temperature=float(env_vars["llm_temperature"])
        python_version=env_vars["python_version"]
        test_code, import_statements = _generate_unit_tests(
            provider=client,
            model_arg=model_arg,
            llm_test_prompt=env_vars["llm_test_prompt"],
            llm_import_prompt=env_vars["llm_import_prompt"],
            llm_temperature=llm_temperature,
            python_version=python_version,
            requirements_txt=env_vars["requirements_txt"],
            function_names=function_names,
            source_code=source_code,
            source_code_path=str(source_code_path)
        )

        if test_code:
            save_test_file(
                    Path(env_vars["source_dir"]),
                    Path(env_vars["generated_tests_dir"]),
                    source_code_path,
                    test_code
                )

            test_code, test_file_failure, total_test_case, passed_count = run_each_pytest_function_individually(client, model_arg, llm_temperature, 
                                                              python_version,env_vars["requirements_txt"],
                                                              env_vars["llm_resolve_prompt"], env_vars["llm_unique_import_prompt"], env_vars["llm_pytest_fixture_prompt"],
                                                              env_vars["llm_test_cases_prompt"], env_vars["llm_cleanup_prompt"], 
                                                              import_statements, source_code, test_code, Path(env_vars["temp_test_file"]))

            if test_code:
                save_test_file(
                        Path(env_vars["source_dir"]),
                        Path(env_vars["final_dir"]),
                        source_code_path,
                        test_code
                    )
                
            if test_file_failure:
                save_test_file(
                        Path(env_vars["source_dir"]),
                        Path(env_vars["err_dir"]),
                        source_code_path,
                        test_file_failure
                    )
            
    except Exception as e:
        logger.error(f"Failed processing {source_code_path}: {e}")

    logger.info(f"End Processing file: {source_code_path}\n")
    return passed_count, total_test_case


def main() -> NoReturn:
    """
    Main entry point for the test generation and evaluation pipeline.

    This function performs the following steps:
        1. Loads environment variables from the .env file.
        2. Initializes the appropriate LLM client (OpenAI or Azure).
        3. Recursively finds all Python source files in the configured source directory.
        4. For each source file:
            - Extracts public functions/classes.
            - Generates and evaluates unit test cases using an LLM.
            - Aggregates and logs test pass statistics.
        5. Logs a tabulated summary of the results using `tabulate`.

    Raises:
        Exception: If environment initialization or LLM setup fails.

    Returns:
        NoReturn: This function does not return; it completes by logging and possibly calling `sys.exit`.
    """
    try:
        logger.info("Initializing environment, LLM, and source discovery...")
        env_vars = _load_env_variables()
        client, model_arg = _initialize_llm(env_vars)
        source_code_files = _get_python_files(env_vars["source_dir"])
        logger.info("Initialization complete.")
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        raise

    test_stats = []
    for path in source_code_files:
        passed_count, total_test_case  = _process_file(path, client, model_arg, env_vars)
        test_stats.append({
        "filename": path,
        "total_test_cases_passed": passed_count,
        "total_test_cases": total_test_case,
        "percentage_passed (%)": (passed_count / total_test_case * 100) if total_test_case > 0 else 0.0
        })
    test_stats_df = pd.DataFrame(test_stats)
    # test_stats_df.index = test_stats_df.index + 1
    # logger.info(test_stats_df.head())
    
    logger.info("\n" + tabulate(test_stats_df, headers='keys', tablefmt='grid'))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
    finally:
        sys.exit(0)        
