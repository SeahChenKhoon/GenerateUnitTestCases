import pytest
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings


def test_initialise_prompt_returns_correct_structure():
    agent = "test_agent"
    mock_config = {"placeholder": "value"}
    mock_prompt = "This is a {$placeholder} test."

def test_initialise_prompt_handles_missing_placeholder():
    agent = "test_agent"
    mock_config = {}
    mock_prompt = "This is a {$placeholder} test."

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    mock_settings = {"setting": "value"}