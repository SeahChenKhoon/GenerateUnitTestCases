import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    with patch('yaml.load') as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch('yaml.safe_load') as mock_safe_load:
        yield mock_safe_load

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {'key1': 'value1', 'key2': 'value2'}
    prompt_structure = "This is a prompt with {$key1} and {$key2}."

    with patch('builtins.open', mock_open(read_data=prompt_structure)), \
         patch('yaml.load', return_value=config_values):
        result = initialise_prompt(agent)
        assert result == "This is a prompt with value1 and value2."

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_values = {'key1': 'value1'}
    prompt_structure = "This is a prompt with {$key1} and {$key2}."

    with patch('builtins.open', mock_open(read_data=prompt_structure)), \
         patch('yaml.load', return_value=config_values):
        result = initialise_prompt(agent)
        expected_result = "This is a prompt with value1 and {$key2}."
        assert result == expected_result

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "non_existent_agent"

def test_initialise_prompt_invalid_yaml(mock_config_path):
    agent = "test_agent"

def test_initialise_settings_success():
    agent = "test_agent"
    settings_data = {'setting1': 'value1', 'setting2': 'value2'}
    mock_file_data = yaml.dump(settings_data)
    
    with patch('builtins.open', mock_open(read_data=mock_file_data)) as mock_file:
        with patch('yaml.safe_load', return_value=settings_data) as mock_safe_load:
            result = initialise_settings(agent)
            assert result == settings_data
            mock_safe_load.assert_called_once()
            mock_file.assert_called_once_with('./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml')

def test_initialise_settings_file_not_found(mock_config_path):
    agent = "non_existent_agent"

def test_initialise_settings_invalid_yaml(mock_config_path):
    agent = "test_agent"