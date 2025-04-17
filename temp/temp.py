import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch


def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml_content = "placeholder_value: test_value"
    prompt_txt_content = "This is a {$placeholder_value} test."


def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
    assert result is None


def test_initialise_settings_success():
    agent = "test_agent"
    llm_settings_content = "key: value"


def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
    assert result is None