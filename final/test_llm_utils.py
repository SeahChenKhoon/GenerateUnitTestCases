import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch


def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "This is a {$key} prompt."
    expected_prompt = "This is a value prompt."

def test_initialise_prompt_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_yaml = "setting_key: setting_value"
    expected_settings = {"setting_key": "setting_value"}

def test_initialise_settings_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None
