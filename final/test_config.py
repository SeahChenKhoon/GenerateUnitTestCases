import pytest
import os
from unittest.mock import patch
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    actual_api_name = default_settings.API_NAME
    actual_api_v1_str = default_settings.API_V1_STR
    actual_logger_config_path = default_settings.LOGGER_CONFIG_PATH
    assert actual_api_name == expected_api_name, "API_NAME does not match the expected default value"
    assert actual_api_v1_str == expected_api_v1_str, "API_V1_STR does not match the expected default value"
    assert actual_logger_config_path == expected_logger_config_path, "LOGGER_CONFIG_PATH does not match the expected default value"

def test_settings_override_values():
    override_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict(os.environ, override_values):
        overridden_settings = Settings()
    assert overridden_settings.API_NAME == override_values["API_NAME"], "API_NAME does not match the overridden value"
    assert overridden_settings.API_V1_STR == override_values["API_V1_STR"], "API_V1_STR does not match the overridden value"
    assert overridden_settings.LOGGER_CONFIG_PATH == override_values["LOGGER_CONFIG_PATH"], "LOGGER_CONFIG_PATH does not match the overridden value"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": None,
        "LOGGER_CONFIG_PATH": []
    }
    with pytest.raises(ValueError):
        Settings(**invalid_values)