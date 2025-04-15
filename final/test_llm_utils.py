import os
import re
import yaml

def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "Hello, {$key}!"
    expected_prompt = "Hello, value!"

def test_initialise_settings_success():
    agent = "test_agent"
    llm_settings_yaml = "setting_key: setting_value"
    expected_settings = {"setting_key": "setting_value"}
