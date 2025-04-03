import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_valid_agent(mocker):
    mock_config_values = {'placeholder1': 'value1', 'placeholder2': 'value2'}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

    mocker.patch('builtins.open', mock_open(read_data=yaml.dump(mock_config_values)))
    mocker.patch('yaml.load', return_value=mock_config_values)
    mocker.patch('re.finditer', return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure))
    mocker.patch('re.sub', side_effect=lambda pattern, repl, string: string.replace(pattern, repl))

    result = initialise_prompt('valid_agent')
    expected_result = "This is a value1 and value2 test."

    assert result == expected_result

def test_initialise_prompt_invalid_agent(mocker):
    mocker.patch('builtins.open', side_effect=FileNotFoundError)
    mocker.patch('yaml.load', return_value={})

    result = initialise_prompt('invalid_agent')
    assert result is None

def test_initialise_settings_valid_agent(mocker):
    mock_llm_settings = {'setting1': 'value1', 'setting2': 'value2'}

    mocker.patch('builtins.open', mock_open(read_data=yaml.dump(mock_llm_settings)))
    mocker.patch('yaml.safe_load', return_value=mock_llm_settings)

    result = initialise_settings('valid_agent')
    assert result == mock_llm_settings

def test_initialise_settings_invalid_agent(mocker):
    mocker.patch('builtins.open', side_effect=FileNotFoundError)
    mocker.patch('yaml.safe_load', return_value={})

    result = initialise_settings('invalid_agent')
    assert result is None