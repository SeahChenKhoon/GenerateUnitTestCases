import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest


def test_initialise_settings_exception():
    agent = "test_agent"
