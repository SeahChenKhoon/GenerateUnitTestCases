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
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_values():
    return {"placeholder": "value"}

@pytest.fixture
def mock_llm_settings():
    return {"setting1": "value1", "setting2": "value2"}

def test_initialise_prompt_success(mock_config_path, mock_prompt_file_content, mock_config_values):
    agent = "test_agent"
    config_yaml_path = f"{mock_config_path}/{agent}/config.yaml"
    prompt_txt_path = f"{mock_config_path}/{agent}/prompt.txt"

def test_initialise_prompt_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.load", side_effect=yaml.YAMLError):
            result = initialise_prompt(agent)
            assert result is None

def test_initialise_settings_success(mock_config_path, mock_llm_settings):
    agent = "test_agent"
    llm_settings_yaml_path = f"{mock_config_path}/{agent}/llm_settings.yaml"