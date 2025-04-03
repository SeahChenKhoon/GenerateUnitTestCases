import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success(mocker):
    mocker.patch("builtins.open", mock_open(read_data="Hello, {$name}!"))
    mocker.patch("yaml.load", return_value={"name": "World"})
    mocker.patch("os.path.exists", return_value=True)

    result = initialise_prompt("test_agent")
    assert result == "Hello, World!"

def test_initialise_prompt_missing_config_file(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    mocker.patch("os.path.exists", return_value=True)

    with pytest.raises(FileNotFoundError):
        initialise_prompt("test_agent")

def test_initialise_prompt_invalid_yaml(mocker):
    mocker.patch("builtins.open", mock_open(read_data="Hello, {$name}!"))
    mocker.patch("yaml.load", side_effect=yaml.YAMLError)
    mocker.patch("os.path.exists", return_value=True)

    with pytest.raises(yaml.YAMLError):
        initialise_prompt("test_agent")

def test_initialise_settings_success(mocker):
    mock_yaml_data = {"setting1": "value1", "setting2": "value2"}
    mocker.patch("builtins.open", mock_open(read_data=yaml.dump(mock_yaml_data)))
    mocker.patch("yaml.safe_load", return_value=mock_yaml_data)
    mocker.patch("os.path.exists", return_value=True)

    result = initialise_settings("test_agent")
    assert result == mock_yaml_data

def test_initialise_settings_missing_config_file(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    mocker.patch("os.path.exists", return_value=True)

    with pytest.raises(FileNotFoundError):
        initialise_settings("test_agent")

def test_initialise_settings_invalid_yaml(mocker):
    mocker.patch("builtins.open", mock_open(read_data="invalid_yaml"))
    mocker.patch("yaml.safe_load", side_effect=yaml.YAMLError)
    mocker.patch("os.path.exists", return_value=True)

    with pytest.raises(yaml.YAMLError):
        initialise_settings("test_agent")