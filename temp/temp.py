import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_values = {"placeholder1": "value1", "placeholder2": "value2"}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_values = {"placeholder1": "value1"}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

def test_initialise_prompt_exception():
    agent = "test_agent"

def test_initialise_settings_success():
    agent = "test_agent"
    mock_settings = {"setting1": "value1", "setting2": "value2"}

def test_initialise_settings_exception():
    agent = "test_agent"