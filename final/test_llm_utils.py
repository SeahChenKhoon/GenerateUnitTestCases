import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_files():
    prompt_content = "Hello, {$name}!"
    config_content = "name: World"
    llm_settings_content = "setting: value"
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=llm_settings_content).return_value,
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
    llm_settings_content = "setting: value"
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=llm_settings_content).return_value,
    ]
    return m_open
import pytest
from unittest.mock import mock_open, patch

def test_initialise_prompt():
    agent = "test_agent"
    expected_prompt = "Hello, World!"
    mock_config_values = {'placeholder': 'World'}
    mock_prompt_structure = "Hello, {$placeholder}!"

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=mock_config_values):
            result = initialise_prompt(agent)
            assert result == expected_prompt

import pytest
from unittest.mock import mock_open, patch
import yaml

def test_initialise_settings():
    agent = "test_agent"
    expected_settings = {"setting": "value"}
    mock_data = yaml.dump(expected_settings)

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = initialise_settings(agent)
        assert result == expected_settings
