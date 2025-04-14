import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch


def test_initialise_settings_exception():
    agent = "test_agent"
    with patch("theory_evaluation.llm_utils.open", side_effect=Exception("File not found")) as mock_file:
        result = initialise_settings(agent)
        assert result is None
        mock_file.assert_called_once_with(f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml")
