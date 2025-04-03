import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {"placeholder": "value"}
    prompt_structure = "This is a {$placeholder} test."

    with patch("builtins.open", mock_open(read_data=yaml.dump(config_values))) as mock_file:
        with patch("yaml.load", return_value=config_values):
            with patch("re.finditer", return_value=[re.Match]):
                with patch("re.sub", return_value="This is a value test."):
                    result = initialise_prompt(agent)
                    assert result == "This is a value test."
                    mock_file.assert_called_with("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.load", side_effect=Exception("No configuration path to the prompt given.")):
            result = initialise_prompt(agent)
            assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    llm_settings = {"setting": "value"}

    with patch("builtins.open", mock_open(read_data=yaml.dump(llm_settings))) as mock_file:
        with patch("yaml.safe_load", return_value=llm_settings):
            result = initialise_settings(agent)
            assert result == llm_settings
            mock_file.assert_called_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.safe_load", side_effect=Exception("No configuration path to the llm settings given.")):
            result = initialise_settings(agent)
            assert result is None