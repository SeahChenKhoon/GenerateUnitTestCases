import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {"key1": "value1", "key2": "value2"}
    prompt_structure = "This is a {$key1} and {$key2} test."

def test_initialise_prompt_no_config_path():
    agent = "test_agent"

def test_initialise_settings_success():
    agent = "test_agent"
    llm_settings = {"setting1": "value1", "setting2": "value2"}

def test_initialise_settings_no_config_path():
    agent = "test_agent"
