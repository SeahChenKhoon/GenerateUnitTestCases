import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch


def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {'key1': 'value1', 'key2': 'value2'}
    prompt_structure = "This is a {$key1} and {$key2} test."

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with patch('theory_evaluation.llm_utils.open', side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_data = {'setting1': 'value1', 'setting2': 'value2'}

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch('theory_evaluation.llm_utils.open', side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
