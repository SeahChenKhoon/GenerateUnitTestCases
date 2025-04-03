import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {"placeholder": "value"}
    prompt_structure = "This is a {$placeholder} test."
    expected_prompt = "This is a value test."

    with patch("builtins.open", mock_open(read_data=yaml.dump(config_values))) as mock_file:
        with patch("yaml.load", return_value=config_values):
            with patch("re.finditer", return_value=[re.MatchObject()]):
                with patch("re.sub", return_value=expected_prompt):
                    result = initialise_prompt(agent)
                    assert result == expected_prompt
                    assert mock_file.call_count == 2
                    assert hasattr(mock_file(), "read")

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_data = {"setting_key": "setting_value"}

    with patch("builtins.open", mock_open(read_data=yaml.dump(settings_data))) as mock_file:
        with patch("yaml.safe_load", return_value=settings_data):
            result = initialise_settings(agent)
            assert result == settings_data
            assert mock_file.call_count == 1
            assert hasattr(mock_file(), "read")

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None