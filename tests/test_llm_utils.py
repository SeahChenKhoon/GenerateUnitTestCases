import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_values = {'placeholder1': 'value1', 'placeholder2': 'value2'}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_config_values))) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            with patch("re.finditer", return_value=[re.MatchObject()]):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace(pattern, repl)):
                    result = initialise_prompt(agent)
                    assert result == "This is a value1 and value2 test."
                    mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml")
                    mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt", "r")

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    mock_settings = {'setting1': 'value1', 'setting2': 'value2'}

    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_settings))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_settings):
            result = initialise_settings(agent)
            assert result == mock_settings
            mock_file.assert_called_once_with(f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml")

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None