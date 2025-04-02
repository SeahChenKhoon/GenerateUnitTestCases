import pytest
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_with_valid_data():
    mock_yaml_data = {'name': 'test_agent'}
    mock_prompt_text = "Hello, {$name}!"
    expected_prompt = "Hello, test_agent!"
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_prompt_text)) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_data):
            result = initialise_prompt(agent)
            mock_file.assert_called_with(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt", "r")
            assert result == expected_prompt

def test_initialise_prompt_with_missing_placeholder():
    mock_yaml_data = {'name': 'test_agent'}
    mock_prompt_text = "Hello, {$username}!"
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_prompt_text)) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_data):
            result = initialise_prompt(agent)
            mock_file.assert_called_with(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt", "r")
            assert result == mock_prompt_text

def test_initialise_prompt_with_exception():
    agent = "test_agent"
    with patch("builtins.open", side_effect=Exception("File not found")):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_with_valid_data():
    mock_yaml_data = {'setting': 'value'}
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="setting: value")) as mock_file:
        with patch("yaml.safe_load", return_value=mock_yaml_data):
            result = initialise_settings(agent)
            mock_file.assert_called_with(f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml")
            assert result == mock_yaml_data

def test_initialise_settings_with_exception():
    agent = "test_agent"
    with patch("builtins.open", side_effect=Exception("File not found")):
        result = initialise_settings(agent)
        assert result is None