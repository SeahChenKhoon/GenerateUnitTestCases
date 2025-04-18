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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

import pytest
from unittest import mock

def test_initialise_prompt_raises_exception_on_missing_config_file():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        with pytest.raises(FileNotFoundError):
            initialise_prompt("agent_name")
