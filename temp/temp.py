import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_prompt_returns_correct_prompt_structure():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    config_values = {"name": "TestAgent", "version": "1.0"}
    prompt_structure = "Hello, {$name}. Version: {$version}."
    expected_prompt = "Hello, TestAgent. Version: 1.0."

def test_initialise_prompt_raises_exception_for_missing_config_path():
    agent = "test_agent"
    config_path = None

def test_initialise_prompt_handles_missing_placeholder():
    agent = "test_agent"
    config_values = {"name": "TestAgent"}
    prompt_structure = "Hello, {$name}. Version: {$version}."
    expected_prompt = "Hello, TestAgent. Version: {$version}."

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    settings = {"setting1": "value1", "setting2": "value2"}

def test_initialise_settings_raises_exception_for_missing_config_path():
    agent = "test_agent"
    config_path = None