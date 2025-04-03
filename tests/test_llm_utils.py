```python
import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_yaml = "key: value"
    mock_prompt_txt = "This is a {$key} prompt."
    expected_prompt = "This is a value prompt."

    with patch("builtins.open", mock_open(read_data=mock_config_yaml)) as mock_file:
        with patch("yaml.load", return_value={"key": "value"}):
            with patch("re.finditer", return_value=[re.match(r"\{\$(\w+)\}", "{$key}")]):
                with patch("re.sub", return_value=expected_prompt):
                    result = initialise_prompt(agent)
                    assert result == expected_prompt
                    mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml")
                    mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt", "r")

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    mock_llm_settings_yaml = "setting_key: setting_value"
    expected_settings = {"setting_key": "setting_value"}

    with patch("builtins.open", mock_open(read_data=mock_llm_settings_yaml)) as mock_file:
        with patch("yaml.safe_load", return_value=expected_settings):
            result = initialise_settings(agent)
            assert result == expected_settings
            mock_file.assert_called_once_with(f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml")

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
```