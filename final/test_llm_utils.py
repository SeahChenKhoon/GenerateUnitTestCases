
import os
import re
import yaml
def test_initialise_prompt_success():
    agent = "test_agent"
    config_yaml = "placeholder_value: test_value"
    prompt_txt = "This is a {$placeholder_value} test."


import os
import re
import yaml
def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    config_yaml = "another_value: test_value"
    prompt_txt = "This is a {$placeholder_value} test."


import os
import re
import yaml
def test_initialise_prompt_exception():
    agent = "test_agent"


import os
import re
import yaml
def test_initialise_settings_success():
    agent = "test_agent"
    llm_settings_yaml = "setting_key: setting_value"


import os
import re
import yaml
def test_initialise_settings_exception():
    agent = "test_agent"

