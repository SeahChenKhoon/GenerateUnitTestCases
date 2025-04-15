import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settingsimport pytest
@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open()) as mock_file:
        yield mock_file

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load") as mock_yaml:
        yield mock_yaml

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load") as mock_yaml_safe:
        yield mock_yaml_safe