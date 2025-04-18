import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

def test_initialise_prompt_returns_correct_prompt_structure():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    config_yaml = "key1: value1\nkey2: value2"
    prompt_txt = "This is a {$key1} and {$key2} test."
    expected_prompt = "This is a value1 and value2 test."

def test_initialise_prompt_handles_missing_placeholder_gracefully():
    agent = "test_agent"
    config_yaml = "key1: value1"
    prompt_txt = "This is a {$key1} and {$key2} test."
    expected_prompt = "This is a value1 and {$key2} test."

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    settings_yaml = "setting1: value1\nsetting2: value2"
    expected_settings = {"setting1": "value1", "setting2": "value2"}