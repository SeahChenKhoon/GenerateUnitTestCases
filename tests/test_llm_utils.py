import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_valid_agent():
    mock_config_values = {'placeholder': 'value'}
    mock_prompt_structure = "This is a {$placeholder} test."
    expected_prompt = "This is a value test."
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_config_values))) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            with patch("re.finditer", return_value=[re.Match]):
                re.Match.group = lambda self, index: 'placeholder'
                re.sub = lambda pattern, repl, string: expected_prompt
                prompt = initialise_prompt("agent_name")
                assert prompt == expected_prompt
                assert mock_file.call_count == 2

def test_initialise_prompt_missing_placeholder():
    mock_config_values = {}
    mock_prompt_structure = "This is a {$placeholder} test."
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_config_values))) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            with patch("re.finditer", return_value=[re.Match]):
                re.Match.group = lambda self, index: 'placeholder'
                re.sub = lambda pattern, repl, string: mock_prompt_structure
                prompt = initialise_prompt("agent_name")
                assert prompt == mock_prompt_structure
                assert mock_file.call_count == 2

def test_initialise_prompt_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        prompt = initialise_prompt("agent_name")
        assert prompt is None

def test_initialise_settings_valid_agent():
    mock_settings = {'setting_key': 'setting_value'}
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_settings))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_settings):
            settings = initialise_settings("agent_name")
            assert settings == mock_settings
            assert mock_file.call_count == 1

def test_initialise_settings_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        settings = initialise_settings("agent_name")
        assert settings is None