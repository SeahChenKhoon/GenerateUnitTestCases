import yaml
from theory_evaluation.llm_utils import initialise_settings
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_settings_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings = {"key": "value"}
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_llm_settings))) as mock_file:
        with patch("yaml.safe_load", return_value=mock_llm_settings):
            result = initialise_settings(agent)
            assert result == mock_llm_settings
            mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/llm_settings.yaml")