import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

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

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data="data")) as mock_file:
        yield mock_file

@patch("builtins.open", new_callable=mock_open, read_data="data")
@patch("yaml.load")
def test_initialise_prompt_returns_correct_prompt_structure(mock_yaml_load, mock_open_file):
    mock_yaml_load.return_value = {'name': 'Test'}
    mock_open_file.side_effect = [
        mock_open(read_data="Hello {$name}").return_value,
        mock_open(read_data="Hello {$name}").return_value
    ]
    result = initialise_prompt("agent")
    assert result == "Hello Test"

def test_initialise_prompt_raises_exception_on_missing_config():
    with patch("builtins.open", mock_open()) as mock_open_file:
        mock_open_file.side_effect = FileNotFoundError
        result = initialise_prompt("agent")
        assert result is None

def test_initialise_prompt_handles_missing_placeholder():
    mock_open_file = mock_open(read_data="Hello {$name}")
    mock_yaml_load = patch("yaml.load", return_value={}).start()
    with patch("builtins.open", mock_open_file):
        result = initialise_prompt("agent")
    assert result == "Hello {$name}"
    mock_yaml_load.stop()

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load") as mock_yaml:
        yield mock_yaml

@pytest.fixture
def mock_config_path():
    with patch("os.getenv", return_value="./theory_evaluation/evaluator/prompts"):
        yield

def test_initialise_settings_returns_correct_settings(mock_open_file, mock_yaml_safe_load, mock_config_path):
    mock_yaml_safe_load.return_value = {'setting': 'value'}
    mock_open_file.return_value = mock_open(read_data="setting: value").return_value
    result = initialise_settings("agent")
    assert result == {'setting': 'value'}

def test_initialise_settings_raises_exception_on_missing_config(mock_open_file):
    mock_open_file.side_effect = FileNotFoundError
    result = initialise_settings("agent")
    assert result is None