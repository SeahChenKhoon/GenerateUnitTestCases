import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a test prompt with placeholders: {$placeholder1}, {$placeholder2}."

@pytest.fixture
def mock_config_values():
    return {
        "placeholder1": "value1",
        "placeholder2": "value2"
    }

@pytest.fixture
def mock_llm_settings_content():
    return {
        "setting1": "value1",
        "setting2": "value2"
    }

from unittest.mock import patch, mock_open
import yaml
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings_content = {"key": "value"}  # Replace with actual expected content

    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_llm_settings_content))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_llm_settings_content):
            result = initialise_settings(agent)
            assert result == mock_llm_settings_content
            mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/llm_settings.yaml")
