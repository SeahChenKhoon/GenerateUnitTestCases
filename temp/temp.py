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

    def open_side_effect(file_path, *args, **kwargs):
        if "prompt.txt" in file_path:
            return mock_open(read_data=prompt_content).return_value
        elif "config.yaml" in file_path:
            return mock_open(read_data=config_content).return_value
        elif "llm_settings.yaml" in file_path:
            return mock_open(read_data=settings_content).return_value
        else:
            raise FileNotFoundError

    return open_side_effect

from unittest.mock import patch

def test_initialise_settings_no_config():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings("agent_name")
        assert result is None
