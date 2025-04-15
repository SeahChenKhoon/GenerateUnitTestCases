import os
import re
import yaml

def test_initialise_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    settings_yaml = "key: value"
