
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_open_files():
    return {
        "./theory_evaluation/evaluator/prompts/test_agent/config.yaml": "key: value",
        "./theory_evaluation/evaluator/prompts/test_agent/prompt.txt": "This is a sample test."
    }

def test_initialise_prompt(mock_open_files):
    with patch("theory_evaluation.llm_utils.open", mock_open()) as mocked_open:
        mocked_open.side_effect = lambda file_path, mode='r': mock_open(read_data=mock_open_files[file_path]).return_value
        prompt = initialise_prompt("test_agent")
        assert prompt == "This is a sample test."

