import pytest
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings


def test_initialise_prompt_returns_correct_prompt_structure():
    agent = "test_agent"
    expected_prompt = "This is a prompt with a value1 and a value2."

def test_initialise_prompt_handles_missing_placeholder_gracefully():
    agent = "test_agent"
    incomplete_prompt_txt = "This is a prompt with a {$key1} and a {$key3}."
    expected_prompt = "This is a prompt with a value1 and a {$key3}."

def test_initialise_prompt_raises_exception_on_file_not_found():
    agent = "non_existent_agent"

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    expected_settings = {"setting1": "value1", "setting2": "value2"}

def test_initialise_settings_raises_exception_on_file_not_found():
    agent = "non_existent_agent"