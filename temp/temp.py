import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_file_open():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value={"key1": "value1", "key2": "value2"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"setting1": "value1", "setting2": "value2"}):
        yield

import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings

def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        result = initialise_settings(agent)
        assert result is None
