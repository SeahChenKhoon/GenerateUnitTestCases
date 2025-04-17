import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_files():
    prompt_content = "Hello, {$name}!"
    config_content = "name: World"
    settings_content = "setting1: value1\nsetting2: value2"
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=settings_content).return_value
    ]
    return m_open
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_files():
    prompt_content = "Hello, {$name}!"
    config_content = "name: World"
    settings_content = "setting1: value1\nsetting2: value2"
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=settings_content).return_value
    ]
    return m_open
from unittest.mock import mock_open, patch

def test_initialise_prompt_success():
    prompt_content = "Hello, {$name}!"
    config_content = {"name": "World"}
    m_open = mock_open(read_data=prompt_content)
    
    with patch("theory_evaluation.llm_utils.open", m_open):
        with patch("yaml.load", return_value=config_content):
            result = initialise_prompt("agent")
            assert result == "Hello, World!"

from unittest.mock import mock_open, patch

def test_initialise_prompt_missing_placeholder(mock_open_files):
    prompt_content = "Hello, {$missing}!"
    mock_open_files.side_effect = [
        mock_open(read_data="name: World").return_value,
        mock_open(read_data=prompt_content).return_value
    ]
    with patch("theory_evaluation.llm_utils.open", mock_open_files):
        with patch("yaml.load", return_value={"name": "World"}):
            result = initialise_prompt("agent")
            assert result == "Hello, {$missing}!"

from unittest.mock import patch

def test_initialise_prompt_exception_handling():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt("agent")
        assert result is None

from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_open_files():
    prompt_content = "prompt content"
    m_open = mock_open(read_data=prompt_content)
    return m_open

def test_initialise_settings_success(mock_open_files):
    with patch("theory_evaluation.llm_utils.open", mock_open_files):
        with patch("yaml.safe_load", return_value={"setting1": "value1", "setting2": "value2"}):
            result = initialise_settings("agent")
            assert result == {"setting1": "value1", "setting2": "value2"}

from unittest.mock import patch

def test_initialise_settings_exception_handling():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings("agent")
        assert result is None
