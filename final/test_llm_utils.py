import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_filesystem():
    with patch("builtins.open", mock_open(read_data=mock_config_yaml)) as mock_file:
        yield mock_file

@pytest.fixture
def mock_prompt_file():
    with patch("builtins.open", mock_open(read_data=mock_prompt_txt)) as mock_file:
        yield mock_file

@pytest.fixture
def mock_llm_settings_file():
    with patch("builtins.open", mock_open(read_data=mock_llm_settings_yaml)) as mock_file:
        yield mock_file

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    prompt_txt = "This is a test prompt with placeholders: {$placeholder1} and {$missing_placeholder}."
    mock_config_yaml = "placeholder1: value1\n"
    expected_prompt = "This is a test prompt with placeholders: value1 and {$missing_placeholder}."

    with patch("builtins.open", mock_open(read_data=prompt_txt)) as mock_file:
        with patch("os.path.exists", return_value=True):
            with patch("yaml.load", return_value={"placeholder1": "value1"}):
                prompt_structure = initialise_prompt(agent)

    assert prompt_structure == expected_prompt

def test_initialise_settings_normal_behavior():
    agent = "test_agent"
    expected_settings = {"setting1": "value1", "setting2": "value2"}
    mock_llm_settings_yaml = yaml.dump(expected_settings)

    with patch("builtins.open", mock_open(read_data=mock_llm_settings_yaml)) as mock_file:
        result = initialise_settings(agent)
        assert result == expected_settings
        mock_file.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")

def test_initialise_settings_invalid_agent():
    agent = "invalid_agent"
    mock_llm_settings_yaml = "key: value"

    with patch("builtins.open", mock_open(read_data=mock_llm_settings_yaml)) as mock_file:
        with patch("yaml.safe_load", return_value={"key": "value"}):
            result = initialise_settings(agent)
            assert result == {"key": "value"}
            mock_file.assert_called_once_with("./theory_evaluation/evaluator/prompts/invalid_agent/llm_settings.yaml")

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    config_path = None

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    config_path = None