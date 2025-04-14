import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_settings_no_config_path():
    agent = "test_agent"
