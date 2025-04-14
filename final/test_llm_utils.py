import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    prompt_content = "Hello, {$name}!"
    config_content = "name: World"
    expected_output = "Hello, World!"

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_content = {"setting1": "value1", "setting2": "value2"}

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
