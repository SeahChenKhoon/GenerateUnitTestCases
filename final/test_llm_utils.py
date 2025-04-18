import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

def test_initialise_prompt_returns_correct_structure():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "Hello, {$key}!"
    expected_prompt = "Hello, value!"

def test_initialise_prompt_handles_missing_placeholder():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "Hello, {$missing_key}!"
    expected_prompt = "Hello, {$missing_key}!"

def test_initialise_prompt_raises_exception_for_missing_file():
    agent = "test_agent"

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    settings_yaml = "setting_key: setting_value"
    expected_settings = {"setting_key": "setting_value"}

def test_initialise_settings_raises_exception_for_missing_file():
    agent = "test_agent"

def test_initialise_prompt_handles_empty_prompt():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = ""

def test_initialise_settings_handles_empty_settings():
    agent = "test_agent"
    settings_yaml = ""