import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None

def test_initialise_settings_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None
