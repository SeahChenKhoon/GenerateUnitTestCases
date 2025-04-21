import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch
from unittest.mock import mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    return {
        "key1": "value1",
        "key2": "value2"
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with placeholders: {$key1} and {$key2}."

@pytest.fixture
def mock_llm_settings():
    return {
        "setting1": "value1",
        "setting2": "value2"
    }

def test_initialise_prompt_success(mock_config_path, mock_yaml_load, mock_prompt_structure):
    agent = "test_agent"
    expected_prompt = "This is a test prompt with placeholders: value1 and value2."

def test_initialise_prompt_missing_placeholder(mock_config_path, mock_yaml_load):
    agent = "test_agent"
    prompt_structure = "This is a test prompt with a missing placeholder: {$missing_key}."
    expected_prompt = "This is a test prompt with a missing placeholder: {$missing_key}."

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "test_agent"

def test_initialise_settings_success(mock_config_path, mock_llm_settings):
    agent = "test_agent"

def test_initialise_settings_file_not_found(mock_config_path):
    agent = "test_agent"