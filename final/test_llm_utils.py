import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a test prompt with a placeholder: {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a test prompt with a placeholder: {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """