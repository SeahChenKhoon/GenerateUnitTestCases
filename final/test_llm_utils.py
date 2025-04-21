import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_open_prompt():
    m = mock_open(read_data="Hello, {$key}!")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load", return_value={"key": "value"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_prompt_normal_behavior():
    agent = "test_agent"
    mock_yaml_content = '{"placeholder": "value"}'
    mock_prompt_content = "Hello, {$placeholder}!"
    
    with patch("builtins.open", mock_open(read_data=mock_yaml_content)) as mock_file_yaml, \
         patch("builtins.open", mock_open(read_data=mock_prompt_content)) as mock_file_prompt, \
         patch("yaml.load", return_value={"placeholder": "value"}):
        
        result = initialise_prompt(agent)
        assert result == "Hello, value!"

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_values = {}
    mock_prompt_structure = "Hello, {$key}!"

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)), \
         patch("yaml.load", return_value=mock_config_values):
        result = initialise_prompt(agent)

    assert result == "Hello, {$key}!"

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
    assert result is None