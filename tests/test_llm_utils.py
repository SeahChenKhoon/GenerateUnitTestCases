import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success(mocker):
    mocker.patch('builtins.open', mock_open(read_data='Hello {$name}'))
    mocker.patch('yaml.load', return_value={'name': 'World'})
    mocker.patch('re.finditer', return_value=[re.Match('{$name}', 0, 7)])
    mocker.patch('re.sub', return_value='Hello World')

    result = initialise_prompt('test_agent')
    assert result == 'Hello World'

def test_initialise_prompt_no_config_path(mocker):
    mocker.patch('builtins.open', side_effect=FileNotFoundError)
    mocker.patch('yaml.load', return_value={})
    mocker.patch('re.finditer', return_value=[])

    result = initialise_prompt('test_agent')
    assert result is None

def test_initialise_settings_success(mocker):
    mocker.patch('builtins.open', mock_open(read_data='key: value'))
    mocker.patch('yaml.safe_load', return_value={'key': 'value'})

    result = initialise_settings('test_agent')
    assert result == {'key': 'value'}

def test_initialise_settings_no_config_path(mocker):
    mocker.patch('builtins.open', side_effect=FileNotFoundError)
    mocker.patch('yaml.safe_load', return_value={})

    result = initialise_settings('test_agent')
    assert result is None