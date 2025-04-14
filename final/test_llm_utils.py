import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt():
    agent = "test_agent"
    config_values = {"placeholder1": "value1", "placeholder2": "value2"}
    prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
    assert result is None

def test_initialise_settings():
    agent = "test_agent"
    llm_settings = {"setting1": "value1", "setting2": "value2"}

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
    assert result is None
