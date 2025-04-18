import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"setting1": "value1", "setting2": "value2"}) as mock:
        yield mock

@pytest.fixture
def mock_file():
    with patch("builtins.open", mock_open(read_data="data")) as mock:
        yield mock

def test_initialise_settings_returns_correct_settings(mock_yaml_safe_load, mock_file):
    agent = "test_agent"
    settings_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
    result = initialise_settings(agent)
    mock_file.assert_called_once_with(settings_path)
    assert result == {"setting1": "value1", "setting2": "value2"}

import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_yaml_safe_load():
    with patch('yaml.safe_load', return_value={}) as mock:
        yield mock

@pytest.fixture
def mock_file():
    with patch('builtins.open', mock_open(read_data="")) as mock:
        yield mock

def test_initialise_settings_with_empty_yaml(mock_yaml_safe_load, mock_file):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {}
