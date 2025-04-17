import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_values = {"placeholder1": "value1", "placeholder2": "value2"}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

from unittest.mock import patch

def test_initialise_prompt_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None

def test_initialise_settings_success():
    agent = "test_agent"
    mock_settings = {"setting1": "value1", "setting2": "value2"}

from unittest.mock import patch

def test_initialise_settings_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None
