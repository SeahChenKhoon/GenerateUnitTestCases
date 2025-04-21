import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }