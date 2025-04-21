import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch
from unittest.mock import mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a test prompt with a placeholder: {$placeholder}."

@pytest.fixture
def mock_config_yaml_content():
    return {"placeholder": "value"}

@pytest.fixture
def mock_llm_settings_yaml_content():
    return {"setting1": "value1", "setting2": "value2"}

def test_initialise_prompt_success(mock_config_path, mock_prompt_file_content, mock_config_yaml_content):
    agent = "test_agent"
    prompt_path = f"{mock_config_path}/{agent}/prompt.txt"
    config_path = f"{mock_config_path}/{agent}/config.yaml"

def test_initialise_prompt_missing_placeholder(mock_config_path, mock_prompt_file_content):
    agent = "test_agent"
    prompt_path = f"{mock_config_path}/{agent}/prompt.txt"
    config_path = f"{mock_config_path}/{agent}/config.yaml"

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError), \
         patch("os.path.exists", return_value=False):
        
        result = initialise_prompt(agent)

def test_initialise_settings_success(mock_config_path, mock_llm_settings_yaml_content):
    agent = "test_agent"
    settings_path = f"{mock_config_path}/{agent}/llm_settings.yaml"

def test_initialise_settings_file_not_found(mock_config_path):
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError), \
         patch("os.path.exists", return_value=False):
        
        result = initialise_settings(agent)