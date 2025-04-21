import yaml
from theory_evaluation.llm_utils import initialise_prompt
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if needed

def test_initialise_prompt_success():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    config_data = "key: value"
    prompt_data = "This is a {$key} prompt."
    expected_prompt = "This is a value prompt."

def test_initialise_prompt_no_placeholder_match():
    agent = "test_agent"
    config_data = "key: value"
    prompt_data = "This is a prompt without placeholders."
    with patch("builtins.open", mock_open(read_data=prompt_data)):
        with patch("yaml.load", return_value={"key": "value"}):
            with patch("re.finditer", return_value=[]):
                result = initialise_prompt(agent)
                assert result == prompt_data