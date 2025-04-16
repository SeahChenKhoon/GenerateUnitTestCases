import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_config_yaml():
    return "key: value"

@pytest.fixture
def mock_prompt_txt():
    return "This is a {$key}."

@pytest.fixture
def mock_settings_yaml():
    return "key: value"
