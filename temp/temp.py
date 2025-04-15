from unittest.mock import patch
from theory_evaluation.evaluator.prompts import initialise_settings

def test_initialise_settings_exception():
    agent = "test_agent"
    with patch("theory_evaluation.evaluator.prompts.open", side_effect=Exception("File not found")):
        result = initialise_settings(agent)
        assert result is None