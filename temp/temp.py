import pytest
import os
import yaml
import re
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
