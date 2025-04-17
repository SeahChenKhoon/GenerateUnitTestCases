import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_prompt_returns_correct_prompt_structure():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    config_data = {'name': 'TestAgent', 'version': '1.0'}
    prompt_data = "Hello, {$name}! Version: {$version}."
    expected_prompt = "Hello, TestAgent! Version: 1.0."

def test_initialise_prompt_handles_missing_placeholder():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    config_data = {'name': 'TestAgent'}
    prompt_data = "Hello, {$name}! Version: {$version}."
    expected_prompt = "Hello, TestAgent! Version: {$version}."

def test_initialise_prompt_raises_exception_on_file_not_found():
    agent = "non_existent_agent"
    config_path = "./theory_evaluation/evaluator/prompts"

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    settings_data = {'setting1': 'value1', 'setting2': 'value2'}

def test_initialise_settings_raises_exception_on_file_not_found():
    agent = "non_existent_agent"
    config_path = "./theory_evaluation/evaluator/prompts"