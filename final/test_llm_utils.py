import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
@pytest.fixture
def mock_yaml_load():
    with patch("theory_evaluation.llm_utils.yaml.load") as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch("theory_evaluation.llm_utils.yaml.safe_load") as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data="This is a test {$placeholder}")) as mock_file:
        yield mock_file