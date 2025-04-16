import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
@pytest.fixture
def mock_open_files():
    prompt_content = "This is a {$placeholder} prompt."
    config_content = '{"placeholder": "test"}'
    settings_content = '{"setting_key": "setting_value"}'
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=settings_content).return_value,
    ]
    return m_open
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
@pytest.fixture
def mock_open_files():
    prompt_content = "This is a {$placeholder} prompt."
    config_content = '{"placeholder": "test"}'
    settings_content = '{"setting_key": "setting_value"}'
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=settings_content).return_value,
    ]
    return m_open
import pytest
from unittest.mock import mock_open, patch

def test_initialise_prompt():
    agent = "test_agent"
    expected_prompt = "This is a value prompt."

    mock_config_values = {"placeholder": "value"}
    mock_prompt_structure = "This is a {$placeholder} prompt."

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)) as mocked_file:
        with patch("yaml.load", return_value=mock_config_values):
            result = initialise_prompt(agent)
            assert result == expected_prompt

import pytest
from unittest.mock import mock_open, patch

def test_initialise_settings():
    agent = "test_agent"
    expected_settings = {"setting_key": "setting_value"}
    mock_yaml_content = "setting_key: setting_value"

    with patch("builtins.open", mock_open(read_data=mock_yaml_content)):
        with patch("yaml.safe_load", return_value=expected_settings):
            settings = initialise_settings(agent)
            assert settings == expected_settings
