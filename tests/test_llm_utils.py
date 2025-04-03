import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_valid_agent():
    mock_config_values = {'placeholder1': 'value1', 'placeholder2': 'value2'}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."
    expected_prompt = "This is a value1 and value2 test."

    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_config_values))) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            with patch("re.finditer", return_value=[re.MatchObject(), re.MatchObject()]):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace(pattern, repl)):
                    result = initialise_prompt("test_agent")
                    assert result == expected_prompt
                    assert mock_file.call_count == 2
                    assert hasattr(mock_file(), 'read')

def test_initialise_prompt_invalid_agent():
    with patch("builtins.open", mock_open(read_data="")):
        with patch("yaml.load", return_value={}):
            result = initialise_prompt("invalid_agent")
            assert result == ""

def test_initialise_settings_valid_agent():
    mock_settings = {'setting1': 'value1', 'setting2': 'value2'}

    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_settings))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_settings):
            result = initialise_settings("test_agent")
            assert result == mock_settings
            assert mock_file.call_count == 1
            assert hasattr(mock_file(), 'read')

def test_initialise_settings_invalid_agent():
    with patch("builtins.open", mock_open(read_data="")):
        with patch("yaml.safe_load", return_value={}):
            result = initialise_settings("invalid_agent")
            assert result == {}