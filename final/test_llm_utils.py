import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import mock_open, patch

def test_initialise_prompt_returns_correct_structure():
    agent = "test_agent"
    config_path = "./theory_evaluation/evaluator/prompts"
    mock_config_values = {"placeholder1": "value1", "placeholder2": "value2"}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."
    m_open = mock_open(read_data=yaml.dump(mock_config_values))
    m_open_prompt = mock_open(read_data=mock_prompt_structure)
    with patch("builtins.open", m_open), patch("builtins.open", m_open_prompt, create=True):
        with patch("yaml.load", return_value=mock_config_values):
            result = initialise_prompt(agent)
    expected_result = "This is a value1 and value2 test."
    assert result == expected_result

def test_initialise_prompt_handles_missing_placeholder():
    agent = "test_agent"
    mock_config_values = {"placeholder1": "value1"}
    mock_prompt_structure = "This is a {$placeholder1} and {$placeholder2} test."
    m_open = mock_open(read_data=yaml.dump(mock_config_values))
    m_open_prompt = mock_open(read_data=mock_prompt_structure)
    with patch("builtins.open", m_open), patch("builtins.open", m_open_prompt, create=True):
        with patch("yaml.load", return_value=mock_config_values):
            result = initialise_prompt(agent)
    expected_result = "This is a value1 and {$placeholder2} test."
    assert result == expected_result

def test_initialise_prompt_prints_error_on_exception():
    agent = "test_agent"
    error_message = "File not found"
    with patch("builtins.open", side_effect=Exception(error_message)), patch("builtins.print") as mock_print:
        initialise_prompt(agent)
        mock_print.assert_called_with(f"{error_message}: No configuration path to the prompt given.")

def test_initialise_settings_returns_correct_settings():
    agent = "test_agent"
    mock_settings = {"setting1": "value1", "setting2": "value2"}
    m_open = mock_open(read_data=yaml.dump(mock_settings))
    with patch("builtins.open", m_open):
        with patch("yaml.safe_load", return_value=mock_settings):
            result = initialise_settings(agent)
    assert result == mock_settings

def test_initialise_settings_prints_error_on_exception():
    agent = "test_agent"
    error_message = "File not found"
    with patch("builtins.open", side_effect=Exception(error_message)), patch("builtins.print") as mock_print:
        initialise_settings(agent)
        mock_print.assert_called_with(f"{error_message}: No configuration path to the llm settings given.")