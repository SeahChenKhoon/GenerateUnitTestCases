import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_files():
    prompt_content = "Hello, {$name}!"
    config_content = '{"name": "World"}'
    llm_settings_content = '{"setting": "value"}'
    mock_files = {
        "./theory_evaluation/evaluator/prompts/test_agent/config.yaml": mock_open(read_data=config_content).return_value,
        "./theory_evaluation/evaluator/prompts/test_agent/prompt.txt": mock_open(read_data=prompt_content).return_value,
        "./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml": mock_open(read_data=llm_settings_content).return_value,
    }
    return mock_files

from unittest.mock import mock_open, patch

def test_initialise_settings(mock_open_files):
    with patch("builtins.open", side_effect=lambda f, *args, **kwargs: mock_open_files[f]):
        result = initialise_settings("test_agent")
        assert result == {"setting": "value"}
