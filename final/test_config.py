from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    settings = default_settings
    assert settings.API_NAME == expected_api_name, "API_NAME does not match the default value"
    assert settings.API_V1_STR == expected_api_v1_str, "API_V1_STR does not match the default value"
    assert settings.LOGGER_CONFIG_PATH == expected_logger_config_path, "LOGGER_CONFIG_PATH does not match the default value"

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        custom_settings = Settings()
    assert custom_settings.API_NAME == custom_values["API_NAME"], "API_NAME does not match the custom value"
    assert custom_settings.API_V1_STR == custom_values["API_V1_STR"], "API_V1_STR does not match the custom value"
    assert custom_settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"], "LOGGER_CONFIG_PATH does not match the custom value"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": "123",
        "API_V1_STR": "456",
        "LOGGER_CONFIG_PATH": "789"
    }
    with patch.dict('os.environ', invalid_values):
        settings = Settings()
        assert settings.API_NAME == "123"
        assert settings.API_V1_STR == "456"
        assert settings.LOGGER_CONFIG_PATH == "789"