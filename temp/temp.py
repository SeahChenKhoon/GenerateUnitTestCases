import os
from theory_evaluation.llm_utils import initialise_settings
import pytest

@pytest.fixture
def mock_files():
    with patch("builtins.open", mock_open(read_data=mock_config_yaml)) as mock_file:
        yield mock_file

@pytest.fixture
def mock_prompt_file():
    with patch("builtins.open", mock_open(read_data=mock_prompt_txt)) as mock_file:
        yield mock_file

@pytest.fixture
def mock_llm_settings_file(tmp_path, monkeypatch):
    agent = "test_agent"
    settings_content = """
    setting1: value1
    setting2: value2
    """
    config_path = tmp_path / "theory_evaluation" / "evaluator" / "prompts" / agent
    config_path.mkdir(parents=True, exist_ok=True)
    settings_file = config_path / "llm_settings.yaml"
    settings_file.write_text(settings_content)

    def mock_open(file, mode='r', *args, **kwargs):
        if file == str(settings_file):
            return settings_file.open(mode)
        return open(file, mode, *args, **kwargs)

    monkeypatch.setattr("builtins.open", mock_open)
    return settings_file

def test_initialise_settings_normal_behavior(mock_llm_settings_file):
    agent = "test_agent"
    expected_settings = {'setting1': 'value1', 'setting2': 'value2'}
    result = initialise_settings(agent)
    assert result == expected_settings