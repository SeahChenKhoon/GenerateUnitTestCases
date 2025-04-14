import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

def test_initialise_prompt():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    config_yaml = "key: value"
    prompt_txt = "Hello, {$key}!"

def test_initialise_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    llm_settings_yaml = "setting_key: setting_value"
