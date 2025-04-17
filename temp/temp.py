import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


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

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"

def test_initialise_settings_success():
    agent = "test_agent"
    settings_yaml = "setting_key: setting_value"
    expected_settings = {"setting_key": "setting_value"}

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"