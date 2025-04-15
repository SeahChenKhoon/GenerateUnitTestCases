import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch

def test_initialise_settings_no_config_path():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None
