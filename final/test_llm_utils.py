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

def test_initialise_prompt():
    config_content = "key: value"
    prompt_content = "Hello, {$key}!"
    mock_files = {
        "./theory_evaluation/evaluator/prompts/test_agent/config.yaml": mock_open(read_data=config_content).return_value,
        "./theory_evaluation/evaluator/prompts/test_agent/prompt.txt": mock_open(read_data=prompt_content).return_value,
    }

    with patch("builtins.open", side_effect=lambda f, *args, **kwargs: mock_files[f]):
        result = initialise_prompt("test_agent")
        assert result == "Hello, value!"

from unittest.mock import mock_open, patch

def test_initialise_prompt_missing_placeholder():
    prompt_content = "Hello, {$name}!"
    config_content = '{}'
    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        mock_file.return_value.read.return_value = prompt_content
        # Call the function or perform the test logic here

from unittest.mock import mock_open, patch

def test_initialise_settings(mock_open_files):
    with patch("builtins.open", side_effect=lambda f, *args, **kwargs: mock_open_files[f]):
        result = initialise_settings("test_agent")
        assert result == {"setting": "value"}
