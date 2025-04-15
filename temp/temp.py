import os
import re
import yaml

def test_initialise_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings = {"setting1": "value1", "setting2": "value2"}
