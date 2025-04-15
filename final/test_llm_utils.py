import os
import re
import yaml

def test_initialise_prompt():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    mock_config_values = {"placeholder1": "value1", "placeholder2": "value2"}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."

def test_initialise_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings = {"setting1": "value1", "setting2": "value2"}
