from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

@pytest.fixture(scope="function", autouse=True)
def mock_environment_variables():
    with patch.dict('os.environ', {
        'API_NAME': 'env_api_name',
        'API_V1_STR': '/env/api/v1',
        'LOGGER_CONFIG_PATH': '/env/path/logging.yml'
    }):
        yield

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        settings = Settings()
        assert settings.API_NAME == "custom_api_name"
        assert settings.API_V1_STR == "/custom/api/v1"
        assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_none_values():
    none_values = {
        "API_NAME": "",
        "API_V1_STR": "",
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', none_values):
        settings = Settings(**none_values)
        assert settings.API_NAME == ""
        assert settings.API_V1_STR == ""
        assert settings.LOGGER_CONFIG_PATH == ""

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": [],
        "LOGGER_CONFIG_PATH": {}
    }
    with pytest.raises(ValueError):
        Settings(**invalid_values)

def test_settings_environment_variables():
    with patch.dict('os.environ', {
        'API_NAME': 'env_api_name',
        'API_V1_STR': '/env/api/v1',
        'LOGGER_CONFIG_PATH': '/env/path/logging.yml'
    }):
        settings = Settings()
        assert settings.API_NAME == "env_api_name"
        assert settings.API_V1_STR == "/env/api/v1"
        assert settings.LOGGER_CONFIG_PATH == "/env/path/logging.yml"