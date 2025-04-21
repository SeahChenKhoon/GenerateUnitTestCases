import yaml
from unittest.mock import patch, mock_open
import pytest
import re

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

def initialise_prompt(agent: str):
    try:
        config_path = "./theory_evaluation/evaluator/prompts"
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        with open(f"{config_path}/{agent}/config.yaml") as file:
            config_values = yaml.load(file, Loader=yaml.loader.BaseLoader)

        with open(f"{config_path}/{agent}/prompt.txt", "r") as file:
            prompt_structure = file.read()

        pattern = r"\{\$(\w+)\}"
        for match in re.finditer(pattern, prompt_structure):
            placeholder = match.group(1)
            if placeholder in config_values:
                prompt_structure = re.sub(
                    r"\{\$" + placeholder + "\}",
                    config_values[placeholder],
                    prompt_structure,
                )
        return prompt_structure

    except Exception as e:
        print(f"{str(e)}: No configuration path to the prompt given.")

@patch("builtins.open", new_callable=mock_open, read_data="Hello, {$missing}!")
@patch("yaml.load", return_value={})
def test_initialise_prompt_missing_placeholder(mock_yaml_load, mock_open_files):
    mock_agent = "test_agent"
    expected_output = "Hello, {$missing}!"
    result = initialise_prompt(mock_agent)
    assert result == expected_output

def test_initialise_prompt_file_not_found():
    mock_agent = "non_existent_agent"
    with patch("builtins.open", mock_open()) as mock_open_files:
        mock_open_files.side_effect = FileNotFoundError
        result = initialise_prompt(mock_agent)
        assert result is None

def initialise_settings(agent: str):
    try:
        config_path = "./theory_evaluation/evaluator/prompts"
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        with open(f"{config_path}/{agent}/llm_settings.yaml") as file:
            return yaml.safe_load(file)

    except Exception as e:
        print(f"{str(e)}: No configuration path to the llm settings given.")

@pytest.fixture
def mock_open_files(mock_agent, mock_config_path):
    m = mock_open(read_data="name: World")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with patch.object(yaml, "safe_load", return_value={"name": "World"}) as mock:
        yield mock

def test_initialise_settings_success(mock_agent, mock_open_files, mock_yaml_safe_load, mock_config_path):
    expected_output = {"name": "World"}
    result = initialise_settings(mock_agent)
    assert result == expected_output
    mock_open_files.assert_called_once_with(f"{mock_config_path}/{mock_agent}/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

if __name__ == "__main__":
    pytest.main()