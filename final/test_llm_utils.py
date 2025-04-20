import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a test prompt with a placeholder {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """

def test_initialise_prompt_success(mock_config_path, mock_prompt_file_content, mock_config_file_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_file:
        with patch("yaml.load", return_value=yaml.safe_load(mock_config_file_content)):
            result = initialise_prompt(agent)
            mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
            mock_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")
            assert result == "This is a test prompt with a placeholder value."

def test_initialise_prompt_missing_placeholder(mock_config_path, mock_prompt_file_content):
    agent = "test_agent"
    incomplete_config_content = """
    another_placeholder: "value"
    """
    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_file:
        with patch("yaml.load", return_value=yaml.safe_load(incomplete_config_content)):
            result = initialise_prompt(agent)
            assert result == "This is a test prompt with a placeholder {$placeholder}."

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success(mock_config_path, mock_llm_settings_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_llm_settings_content)) as mock_file:
        with patch("yaml.safe_load", return_value=yaml.safe_load(mock_llm_settings_content)):
            result = initialise_settings(agent)
            mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/llm_settings.yaml")
            assert result == yaml.safe_load(mock_llm_settings_content)

def test_initialise_settings_file_not_found(mock_config_path):
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None