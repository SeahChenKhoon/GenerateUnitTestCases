import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file():
    return "This is a test prompt with a placeholder {$PLACEHOLDER}."

@pytest.fixture
def mock_config_values():
    return {"PLACEHOLDER": "value"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch("yaml.load", return_value=mock_config_values):
        yield

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch("yaml.safe_load", return_value=mock_config_values):
        yield

def test_initialise_prompt_missing_config(mock_config_path):
    agent = "test_agent"
    prompt_path = f"{mock_config_path}/{agent}/prompt.txt"
    config_path = f"{mock_config_path}/{agent}/config.yaml"

def test_initialise_settings_missing_file(mock_config_path):
    agent = "test_agent"
    settings_path = f"{mock_config_path}/{agent}/llm_settings.yaml"