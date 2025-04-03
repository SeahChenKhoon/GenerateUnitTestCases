import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success(mocker):
    agent = "test_agent"
    config_values = {'placeholder': 'value'}
    prompt_structure = "This is a {$placeholder}."

    mock_open_file = mock_open(read_data=yaml.dump(config_values))
    mocker.patch("builtins.open", mock_open_file)
    mocker.patch("yaml.load", return_value=config_values)
    mocker.patch("re.finditer", return_value=[re.Match()])
    mocker.patch("re.sub", return_value="This is a value.")

    result = initialise_prompt(agent)
    assert result == "This is a value."

def test_initialise_prompt_file_not_found(mocker):
    agent = "test_agent"
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    result = initialise_prompt(agent)
    assert result is None

def test_initialise_settings_success(mocker):
    agent = "test_agent"
    settings_data = {'setting_key': 'setting_value'}

    mock_open_file = mock_open(read_data=yaml.dump(settings_data))
    mocker.patch("builtins.open", mock_open_file)
    mocker.patch("yaml.safe_load", return_value=settings_data)

    result = initialise_settings(agent)
    assert result == settings_data

def test_initialise_settings_file_not_found(mocker):
    agent = "test_agent"
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    result = initialise_settings(agent)
    assert result is None