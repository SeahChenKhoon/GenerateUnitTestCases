import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
from unittest.mock import mock_open, patch

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        result = initialise_prompt(agent)
        assert result is None

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    file_path = f"{config_path}/{agent}/llm_settings.yaml"
    
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        with patch("os.path.exists", return_value=False):
            result = initialise_settings(agent)
            assert result is None