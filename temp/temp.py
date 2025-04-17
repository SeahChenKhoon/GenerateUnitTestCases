import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_prompt_returns_correct_structure():
    agent = "test_agent"
    mock_config = {'name': 'Test Agent', 'version': '1.0'}
    mock_prompt = "Hello, {$name}. Version: {$version}."

def test_initialise_prompt_handles_missing_placeholder():
    agent = "test_agent"
    mock_config = {'name': 'Test Agent'}
    mock_prompt = "Hello, {$name}. Version: {$version}."

def test_initialise_settings_returns_correct_values():
    agent = "test_agent"
    mock_settings = {'setting1': 'value1', 'setting2': 'value2'}