import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
@pytest.fixture
def mock_open_files():
    prompt_content = "This is a test prompt with {$placeholder}."
    config_content = "placeholder: value"
    settings_content = "setting_key: setting_value"
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=settings_content).return_value,
    ]
    return m_open

def test_initialise_prompt():
    with patch("theory_evaluation.llm_utils.open", mock_open_files()) as m_open, \
         patch("theory_evaluation.llm_utils.yaml.load", return_value={"placeholder": "value"}):
        result = initialise_prompt("test_agent")
        assert result == "This is a test prompt with value."
        m_open.assert_has_calls([
            patch("theory_evaluation.llm_utils.open").call(f"./theory_evaluation/evaluator/prompts/test_agent/config.yaml"),
            patch("theory_evaluation.llm_utils.open").call(f"./theory_evaluation/evaluator/prompts/test_agent/prompt.txt", "r")
        ])
