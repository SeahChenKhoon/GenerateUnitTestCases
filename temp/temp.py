import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with a placeholder: {$placeholder}"

@pytest.fixture
def mock_config_values():
    return {"placeholder": "value"}

@pytest.fixture
def mock_llm_settings():
    return {"setting1": "value1", "setting2": "value2"}

import os
import re
import yaml
from unittest.mock import patch, mock_open

def test_initialise_prompt_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_agent = "test_agent"
    mock_prompt_structure = "This is a test prompt with a placeholder: {$placeholder}"
    mock_config_values = {"placeholder": "value"}
    
    mock_yaml_content = yaml.dump(mock_config_values)
    with patch("builtins.open", mock_open(read_data=mock_yaml_content)) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            with patch("re.finditer", return_value=[re.Match]):
                with patch("re.sub", return_value=mock_prompt_structure.replace("{$placeholder}", "value")):
                    result = initialise_prompt(mock_agent)
                    mock_file.assert_any_call(f"{mock_config_path}/{mock_agent}/config.yaml")
                    mock_file.assert_any_call(f"{mock_config_path}/{mock_agent}/prompt.txt", "r")
                    assert result == "This is a test prompt with a placeholder: value"