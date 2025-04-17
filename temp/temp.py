import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch

def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "This is a {$key} test."
    expected_prompt = "This is a value test."

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "This is a {$missing_key} test."
    expected_prompt = "This is a {$missing_key} test."

def test_initialise_prompt_exception():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_yaml = "setting1: value1\nsetting2: value2"
    expected_settings = {'setting1': 'value1', 'setting2': 'value2'}

def test_initialise_settings_exception():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None