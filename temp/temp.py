from unittest.mock import patch
from theory_evaluation.evaluator.prompts import initialise_settings

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch('theory_evaluation.evaluator.prompts.open', side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None