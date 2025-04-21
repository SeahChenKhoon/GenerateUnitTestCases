import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_filesystem():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"key": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    prompt_content = "This is a {$missing} test."
    config_content = {"placeholder": "value"}
    
    with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_file:
        with patch("yaml.load", return_value=config_content):
            result = initialise_prompt(agent)
            assert result == "This is a {$missing} test."

def test_initialise_prompt_file_not_found(mock_filesystem):
    agent = "test_agent"
    mock_filesystem.side_effect = FileNotFoundError
    result = initialise_prompt(agent)
    assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    mock_data = yaml.dump({"key": "value"})
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
        result = initialise_settings(agent)
        assert result == {"key": "value"}
        mock_file.assert_called_once_with(f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml")

def test_initialise_settings_file_not_found(mock_filesystem):
    agent = "test_agent"
    mock_filesystem.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None