import os
import re
import yaml
import pytest
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_file_open():
    with patch("builtins.open", mock_open(read_data="key1: value1\nkey2: value2")) as m:
        yield m

@pytest.fixture
def mock_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        yield

@pytest.mark.parametrize("agent, config_content, prompt_content, expected_output", [
    ("agent1", "key1: value1\nkey2: value2", "Hello {$key1}, welcome to {$key2}!", "Hello value1, welcome to value2!"),
    # Add more test cases as needed
])
def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"
    
    m_open = mock_open()
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value
    ]
    
    with patch("builtins.open", m_open):
        result = initialise_prompt(agent)
        assert result == expected_output

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None