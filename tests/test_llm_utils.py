import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success(mocker):
    agent = "test_agent"
    mock_config_values = {'key1': 'value1', 'key2': 'value2'}
    mock_prompt_structure = "This is a {$key1} and {$key2} test."

    mocker.patch("builtins.open", mock_open(read_data=yaml.dump(mock_config_values)))
    mocker.patch("yaml.load", return_value=mock_config_values)
    mocker.patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure))
    mocker.patch("re.sub", side_effect=lambda pattern, repl, string: string.replace("{$key1}", "value1").replace("{$key2}", "value2"))

    result = initialise_prompt(agent)
    assert result == "This is a value1 and value2 test."

def test_initialise_prompt_file_not_found(mocker):
    agent = "test_agent"
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    result = initialise_prompt(agent)
    assert result is None

def test_initialise_settings_success(mocker):
    agent = "test_agent"
    mock_llm_settings = {'setting1': 'value1', 'setting2': 'value2'}

    mocker.patch("builtins.open", mock_open(read_data=yaml.dump(mock_llm_settings)))
    mocker.patch("yaml.safe_load", return_value=mock_llm_settings)

    result = initialise_settings(agent)
    assert result == mock_llm_settings

def test_initialise_settings_file_not_found(mocker):
    agent = "test_agent"
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    result = initialise_settings(agent)
    assert result is None