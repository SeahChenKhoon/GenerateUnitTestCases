import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt
import pytest
from unittest.mock import patch

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_prompt_success(mock_config_path, mock_yaml_load, mock_prompt_structure):
    agent = "test_agent"
    config_yaml_path = f"{mock_config_path}/{agent}/config.yaml"
    prompt_txt_path = f"{mock_config_path}/{agent}/prompt.txt"

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
    assert result is None

def test_initialise_settings_success(mock_config_path, mock_llm_settings):
    agent = "test_agent"
    llm_settings_yaml_path = f"{mock_config_path}/{agent}/llm_settings.yaml"