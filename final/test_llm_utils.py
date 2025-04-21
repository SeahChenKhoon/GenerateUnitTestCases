import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_data():
    return {
        'key1': 'value1',
        'key2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with placeholders: {$key1} and {$key2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_prompt_success(mock_config_path, mock_yaml_data, mock_prompt_structure):
    agent = "test_agent"
    mock_config_file = yaml.dump(mock_yaml_data)
    expected_prompt = "This is a test prompt with placeholders: value1 and value2."

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_prompt_no_placeholders(mock_config_path):
    agent = "test_agent"
    mock_config_file = yaml.dump({})
    mock_prompt_structure = "This is a test prompt with no placeholders."

def test_initialise_settings_success(mock_config_path, mock_llm_settings):
    agent = "test_agent"
    mock_llm_file = yaml.dump(mock_llm_settings)

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None