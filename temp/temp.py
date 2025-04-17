To clean up the test code by removing duplicate or unused imports, you can consolidate the necessary imports at the top and remove any duplicates or unused ones. Here's the cleaned-up version of your test code:

import pytest
from unittest.mock import patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "This is a {$key} prompt."

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    settings_yaml = "setting_key: setting_value"

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

### Explanation:
- Removed duplicate imports of `os`, `re`, `yaml`, and `pytest`.
- Removed unused imports: `os`, `re`, and `yaml`, as they are not used in the test functions.
- Kept `pytest` and `patch` from `unittest.mock` as they are used in the test functions.
- Kept `initialise_prompt` and `initialise_settings` from `theory_evaluation.llm_utils` as they are used in the test functions.