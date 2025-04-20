import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists") as mock_exists:
        mock_exists.return_value = True
        yield

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load") as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load") as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data="data")) as mock_file:
        yield mock_file
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists") as mock_exists:
        mock_exists.return_value = True
        yield

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load") as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load") as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data="data")) as mock_file:
        yield mock_file