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
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    mock_llm_settings_content = "setting1: value1\nsetting2: value2\n"
    with patch("builtins.open", mock_open(read_data=mock_llm_settings_content)) as mock_file:
        with patch("yaml.safe_load", return_value={"setting1": "value1", "setting2": "value2"}):
            result = initialise_settings(agent)
            assert result == {"setting1": "value1", "setting2": "value2"}
            mock_file.assert_called_once_with(f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml")

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None