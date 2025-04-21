import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path(monkeypatch):
    monkeypatch.setattr('os.environ', {'CONFIG_PATH': './theory_evaluation/evaluator/prompts'})

@pytest.fixture
def mock_yaml_load():
    with patch('yaml.load') as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch('yaml.safe_load') as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_file():
    with patch('builtins.open', mock_open(read_data="Sample prompt with {$placeholder}")) as mock_file:
        yield mock_file

def test_initialise_prompt_success():
    with patch('builtins.open', mock_open(read_data="Sample prompt with {$placeholder}")) as mock_file:
        with patch('yaml.load', return_value={'placeholder': 'value'}):
            result = initialise_prompt('agent_name')
            assert result == "Sample prompt with value"

def test_initialise_prompt_missing_placeholder():
    with patch('builtins.open', mock_open(read_data="Sample prompt with {$placeholder}")) as mock_file:
        with patch('yaml.load', return_value={}) as mock_yaml_load:
            result = initialise_prompt("agent_name")
            assert result == "Sample prompt with {$placeholder}"
            mock_file.assert_any_call("./theory_evaluation/evaluator/prompts/agent_name/prompt.txt", "r")
            mock_yaml_load.assert_called_once()

def test_initialise_prompt_file_not_found():
    with patch('builtins.open', mock_open(read_data="Sample prompt with {$placeholder}")) as mock_file:
        mock_file.side_effect = FileNotFoundError
        result = initialise_prompt("non_existent_agent")
        assert result is None

def test_initialise_prompt_invalid_yaml():
    with patch('builtins.open', mock_open(read_data="Sample prompt with {$placeholder}")) as mock_file:
        with patch('yaml.load', side_effect=yaml.YAMLError):
            result = initialise_prompt("agent_name")
            assert result is None

def test_initialise_settings_success():
    with patch('builtins.open', mock_open(read_data="key: value")) as mock_file:
        with patch('yaml.safe_load', return_value={'key': 'value'}) as mock_yaml_safe_load:
            result = initialise_settings('agent_name')
            assert result == {'key': 'value'}
            mock_file.assert_called_once_with('./theory_evaluation/evaluator/prompts/agent_name/llm_settings.yaml')
            mock_yaml_safe_load.assert_called_once()

def test_initialise_settings_file_not_found():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        result = initialise_settings("non_existent_agent")
        assert result is None

def test_initialise_settings_invalid_yaml():
    with patch('builtins.open', mock_open(read_data="invalid_yaml")) as mock_file:
        with patch('yaml.safe_load', side_effect=yaml.YAMLError):
            result = initialise_settings("some_agent")
            assert result is None