import yaml
from theory_evaluation.llm_utils import initialise_settings
import pytest
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

def test_initialise_settings():
    agent = "test_agent"
    settings_content = """
    key1: value1
    key2: value2
    """
    expected_output = {'key1': 'value1', 'key2': 'value2'}

    with patch("builtins.open", mock_open(read_data=settings_content)):
        with patch("yaml.safe_load", return_value=expected_output):
            result = initialise_settings(agent)
            assert result == expected_output