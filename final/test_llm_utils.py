import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}! Welcome to {$place}."

@pytest.fixture
def mock_config_values():
    return {
        "name": "Alice",
        "place": "Wonderland"
    }

@pytest.fixture
def mock_llm_settings():
    return {
        "model": "gpt-3",
        "temperature": 0.7
    }

def test_initialise_prompt_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_agent = "short_discussion"
    mock_prompt_structure = "Hello, {$name}! Welcome to {$place}."
    mock_config_values = {"name": "Alice", "place": "Wonderland"}

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            result = initialise_prompt(mock_agent)
            expected_prompt = "Hello, Alice! Welcome to Wonderland."
            assert result == expected_prompt
            mock_file.assert_any_call(f"{mock_config_path}/{mock_agent}/config.yaml")
            mock_file.assert_any_call(f"{mock_config_path}/{mock_agent}/prompt.txt", "r")

def test_initialise_settings_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_agent = "refactor_code"
    mock_llm_settings = {"key": "value"}
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_llm_settings))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_llm_settings):
            result = initialise_settings(mock_agent)
            assert result == mock_llm_settings
            mock_file.assert_called_once_with(f"{mock_config_path}/{mock_agent}/llm_settings.yaml")

def test_initialise_settings_invalid_yaml():
    mock_agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.safe_load", side_effect=yaml.YAMLError):
            result = initialise_settings(mock_agent)
            assert result is None