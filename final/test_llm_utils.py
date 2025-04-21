import os
import re
import yaml
import pytest
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

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

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch("os.path.exists", return_value=False):
            result = initialise_prompt(agent)
            assert result is None

def test_initialise_settings_success(mock_config_path, mock_llm_settings_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_llm_settings_content)) as mock_file:
        with patch("os.path.exists", return_value=True):
            result = initialise_settings(agent)
            expected_result = yaml.safe_load(mock_llm_settings_content)
            assert result == expected_result
            mock_file.assert_called_with(f"{mock_config_path}/{agent}/llm_settings.yaml")

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None