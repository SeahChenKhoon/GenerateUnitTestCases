
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "key: value"
    prompt_txt = "This is a {$key} prompt."
    expected_prompt = "This is a value prompt."


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch
def test_initialise_settings_success():
    agent = "test_agent"
    settings_yaml = "key: value"
    expected_settings = {"key": "value"}


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch
def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

