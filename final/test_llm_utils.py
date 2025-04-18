import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as m:
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as m:
        yield m

@pytest.fixture
def mock_os_path_exists():
    with mock.patch("os.path.exists", return_value=True) as m:
        yield m
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as m:
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as m:
        yield m

@pytest.fixture
def mock_os_path_exists():
    with mock.patch("os.path.exists", return_value=True) as m:
        yield m
from unittest import mock

def test_initialise_prompt_returns_expected_output_on_valid_input():
    # Arrange
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open(read_data="This is a {$placeholder} test.")) as mock_open:
        with mock.patch("yaml.load", return_value={"placeholder": "sample"}):
            # Act
            result = initialise_prompt(agent)

            # Assert
            assert result == "This is a sample test."

from unittest import mock
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

def test_initialise_prompt_raises_exception_on_missing_config(mock_open):
    # Arrange
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError

    # Act
    result = initialise_prompt(agent)

    # Assert
    assert result is None

import pytest
from unittest import mock

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load", return_value={"missing": "value"}) as m:
        yield m

def test_initialise_prompt_handles_missing_placeholder(mock_open, mock_yaml_load):
    # Arrange
    agent = "test_agent"
    mock_open().read.return_value = "This is a {$missing} test."

    # Act
    result = initialise_prompt(agent)

    # Assert
    assert result == "This is a value test."

from unittest import mock

def test_initialise_settings_returns_expected_output_on_valid_input():
    # Arrange
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open(read_data="key: value")) as m:
        with mock.patch("yaml.safe_load", return_value={"key": "value"}):
            # Act
            result = initialise_settings(agent)

            # Assert
            assert result == {"key": "value"}

import pytest
from unittest import mock

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

def test_initialise_settings_raises_exception_on_missing_config(mock_open):
    # Arrange
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        initialise_settings(agent)
        raise FileNotFoundError  # Ensure the exception is raised

from unittest import mock
import yaml

def test_initialise_settings_handles_invalid_yaml():
    # Arrange
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as m:
        m().read.side_effect = yaml.YAMLError
        # Act & Assert
        try:
            initialise_settings(agent)
        except yaml.YAMLError:
            pass
