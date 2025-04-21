import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_structure():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_values():
    return {"placeholder": "value"}

@pytest.fixture
def mock_llm_settings():
    return {"setting1": "value1", "setting2": "value2"}
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_structure():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_values():
    return {"placeholder": "value"}

@pytest.fixture
def mock_llm_settings():
    return {"setting1": "value1", "setting2": "value2"}
import pytest
import os
import re
import yaml
from unittest.mock import mock_open, patch

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_config_values = {'key1': 'value1', 'key2': 'value2'}
    mock_prompt_structure = "This is a test prompt with {$key1} and {$key2}."

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            result = initialise_prompt(agent)
            expected_result = "This is a test prompt with value1 and value2."
            assert result == expected_result

import pytest
from unittest.mock import patch
from your_module import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
    assert result is None

def test_initialise_prompt_invalid_yaml(mock_config_path, mock_prompt_structure):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.load", side_effect=yaml.YAMLError):
            result = initialise_prompt(agent)
    assert result is None

import pytest
import yaml
from unittest.mock import mock_open, patch
from your_module import initialise_settings

def test_initialise_settings_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings = {'key': 'value'}

    llm_yaml_path = f"{mock_config_path}/{agent}/llm_settings.yaml"
    
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_llm_settings))):
        with patch("yaml.safe_load", return_value=mock_llm_settings):
            result = initialise_settings(agent)
            assert result == mock_llm_settings

import pytest
from unittest.mock import patch
from your_module import initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

def test_initialise_settings_file_not_found(mock_config_path):
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
    assert result is None

import pytest
from unittest.mock import patch, mock_open
import yaml
from your_module import initialise_settings

def test_initialise_settings_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.safe_load", side_effect=yaml.YAMLError):
            result = initialise_settings(agent)
    assert result is None
