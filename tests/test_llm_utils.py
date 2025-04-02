```python
import pytest
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_with_valid_agent():
    mock_yaml_content = {'name': 'test_agent'}
    mock_prompt_content = "Hello, {$name}!"
    expected_result = "Hello, test_agent!"
    with patch("builtins.open", mock_open(read_data=mock_prompt_content)) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_content):
            result = initialise_prompt("valid_agent")
            mock_file.assert_called_with('./theory_evaluation/evaluator/prompts/valid_agent/prompt.txt', 'r')
            assert result == expected_result

def test_initialise_prompt_with_invalid_agent_raises_exception():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            initialise_prompt("invalid_agent")

def test_initialise_prompt_with_missing_placeholder_in_config():
    mock_yaml_content = {'unused': 'value'}
    mock_prompt_content = "Hello, {$name}!"
    with patch("builtins.open", mock_open(read_data=mock_prompt_content)) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_content):
            result = initialise_prompt("missing_placeholder")
            assert result == "Hello, {$name}!"

def test_initialise_settings_with_valid_agent():
    mock_yaml_content = {'setting': 'value'}
    with patch("builtins.open", mock_open(read_data="setting: value")) as mock_file:
        with patch("yaml.safe_load", return_value=mock_yaml_content):
            result = initialise_settings("valid_agent")
            mock_file.assert_called_with('./theory_evaluation/evaluator/prompts/valid_agent/llm_settings.yaml')
            assert result == mock_yaml_content

def test_initialise_settings_with_invalid_agent_raises_exception():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            initialise_settings("invalid_agent")
```