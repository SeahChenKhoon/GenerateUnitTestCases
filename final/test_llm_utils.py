import os
import re
import yaml

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {'key1': 'value1', 'key2': 'value2'}
    prompt_structure = "This is a {$key1} and {$key2} test."

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_values = {'key1': 'value1'}
    prompt_structure = "This is a {$key1} and {$key2} test."

def test_initialise_settings_success():
    agent = "test_agent"
    settings_data = {'setting1': 'value1', 'setting2': 'value2'}
