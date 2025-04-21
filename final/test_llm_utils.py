import os
import re
import yaml
import pytest
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists") as mock_exists:
        mock_exists.return_value = True
        yield

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load") as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load") as mock_safe_load:
        yield mock_safe_load

def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {"key1": "value1", "key2": "value2"}
    prompt_structure = "This is a {$key1} and {$key2} test."
    expected_output = "This is a value1 and value2 test."

    with patch("builtins.open", mock_open(read_data=prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=config_values):
            result = initialise_prompt(agent)
            assert result == expected_output

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_values = {"key1": "value1"}
    prompt_structure = "This is a {$key1} and {$key2} test."

    with patch("builtins.open", mock_open(read_data=prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=config_values):
            result = initialise_prompt(agent)
            expected_prompt = "This is a value1 and {$key2} test."
            assert result == expected_prompt

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
    assert result is None

def test_initialise_prompt_invalid_yaml():
    agent = "test_agent"
    mock_yaml_content = "key1: value1\nkey2: value2"
    mock_prompt_content = "This is a {$key1} test."

    with patch("builtins.open", mock_open(read_data=mock_prompt_content)) as mock_file:
        with patch("os.path.exists", return_value=True):
            with patch("yaml.load", return_value={"key1": "value1"}):
                prompt_structure = initialise_prompt(agent)
                assert prompt_structure == "This is a value1 test."

def test_initialise_settings_success():
    agent = "test_agent"
    expected_settings = {"setting1": "value1", "setting2": "value2"}
    mock_yaml_content = yaml.dump(expected_settings)

    with patch("builtins.open", mock_open(read_data=mock_yaml_content)):
        with patch("yaml.safe_load", return_value=expected_settings):
            result = initialise_settings(agent)
            assert result == expected_settings

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
    assert result is None

def test_initialise_settings_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml_content")):
        with patch("yaml.safe_load", side_effect=yaml.YAMLError("Invalid YAML")):
            result = initialise_settings(agent)
            assert result is None