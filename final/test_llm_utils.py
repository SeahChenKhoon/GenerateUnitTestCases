
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
def test_initialise_prompt_success():
    agent = "test_agent"
    prompt_content = "Hello, {$name}!"
    config_content = "name: World"


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import os
import re
import yaml
from unittest.mock import patch

def test_initialise_prompt_no_config_path():
    with patch("theory_evaluation.llm_utils.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
def test_initialise_settings_success():
    agent = "test_agent"
    settings_content = "key: value"


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch

def test_initialise_settings_no_config_path():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None

