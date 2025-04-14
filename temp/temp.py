import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch


def test_initialise_settings_file_not_found():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None
