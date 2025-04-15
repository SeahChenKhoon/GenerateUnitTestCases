import os
import re
import yaml

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {"placeholder": "value"}
    prompt_structure = "This is a {$placeholder} test."

def test_initialise_prompt_no_placeholder():
    agent = "test_agent"
    config_values = {}
    prompt_structure = "This is a test."

def test_initialise_settings_success():
    agent = "test_agent"
    llm_settings = {"setting": "value"}
