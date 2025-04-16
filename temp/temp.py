import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
@pytest.fixture
def mock_agent_config():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "This is a {$key} test."
    with patch("theory_evaluation.llm_utils.open", mock_open(read_data=config_yaml)) as mock_file:
        with patch("theory_evaluation.llm_utils.open", mock_open(read_data=prompt_txt)) as mock_prompt_file:
            yield agent, mock_file, mock_prompt_file

@pytest.fixture
def mock_agent_settings():
    agent = "test_agent"
    settings_yaml = "key: value"
    with patch("theory_evaluation.llm_utils.open", mock_open(read_data=settings_yaml)) as mock_file:
        yield agent, mock_file

from unittest.mock import patch

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
