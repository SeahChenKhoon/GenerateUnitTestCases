
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
def test_initialise_prompt_success():
    agent = "test_agent"
    config_values = {'key1': 'value1', 'key2': 'value2'}
    prompt_structure = "This is a {$key1} and {$key2} test."


import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
def test_initialise_settings_success():
    agent = "test_agent"
    settings_data = {'setting1': 'value1', 'setting2': 'value2'}

