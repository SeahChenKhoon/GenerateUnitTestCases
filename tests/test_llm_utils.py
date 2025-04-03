import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_valid_agent():
    mock_yaml_data = {'key': 'value'}
    mock_prompt_structure = "This is a {$key} test."
    expected_result = "This is a value test."
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_yaml_data))) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_data):
            with patch("re.finditer", return_value=[re.Match]):
                re.Match.group = lambda self, _: 'key'
                result = initialise_prompt("agent")
                assert result == expected_result
                assert mock_file.call_count == 2

def test_initialise_prompt_missing_placeholder():
    mock_yaml_data = {'key': 'value'}
    mock_prompt_structure = "This is a {$missing_key} test."
    expected_result = "This is a {$missing_key} test."
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_yaml_data))) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_data):
            result = initialise_prompt("agent")
            assert result == expected_result
            assert mock_file.call_count == 2

def test_initialise_prompt_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt("agent")
        assert result is None

def test_initialise_settings_valid_agent():
    mock_yaml_data = {'setting': 'value'}
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_yaml_data))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_yaml_data):
            result = initialise_settings("agent")
            assert result == mock_yaml_data
            assert mock_file.call_count == 1

def test_initialise_settings_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("agent")
        assert result is None