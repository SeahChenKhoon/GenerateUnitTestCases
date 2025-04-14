import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch


def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {'name': 'TestAgent', 'version': '1.0'}
    prompt_structure = "Hello, my name is {$name} and version is {$version}."

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with patch('theory_evaluation.llm_utils.open', side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_data = {'setting1': 'value1', 'setting2': 'value2'}

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with patch('theory_evaluation.llm_utils.open', side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
