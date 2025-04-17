import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "placeholder_value: 'test_value'"
    prompt_txt = "This is a {$placeholder_value} test."

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_yaml = "another_value: 'test_value'"
    prompt_txt = "This is a {$placeholder_value} test."

def test_initialise_prompt_exception():
    agent = "test_agent"

def test_initialise_settings_success():
    agent = "test_agent"
    settings_yaml = "key: value"

def test_initialise_settings_exception():
    agent = "test_agent"