import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub