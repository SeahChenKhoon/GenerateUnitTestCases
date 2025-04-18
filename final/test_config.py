import pytest
from pydantic import ValidationError
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_default_values():
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    settings = Settings()
    assert settings.API_NAME == expected_api_name
    assert settings.API_V1_STR == expected_api_v1_str
    assert settings.LOGGER_CONFIG_PATH == expected_logger_config_path

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    settings = Settings(**custom_values)
    assert settings.API_NAME == custom_values["API_NAME"]
    assert settings.API_V1_STR == custom_values["API_V1_STR"]
    assert settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": None,
        "LOGGER_CONFIG_PATH": ["invalid", "list"]
    }
    with pytest.raises(ValidationError):
        Settings(**invalid_values)

def test_settings_empty_string_values():
    empty_string_values = {
        "API_NAME": "",
        "API_V1_STR": "",
        "LOGGER_CONFIG_PATH": ""
    }
    settings = Settings(**empty_string_values)
    assert settings.API_NAME == ""
    assert settings.API_V1_STR == ""
    assert settings.LOGGER_CONFIG_PATH == ""

def test_settings_large_input_values():
    large_input_values = {
        "API_NAME": "a" * 1000,
        "API_V1_STR": "/api/" + "v" * 1000,
        "LOGGER_CONFIG_PATH": "/path/" + "logging" * 1000 + ".yml"
    }
    settings = Settings(**large_input_values)
    assert settings.API_NAME == large_input_values["API_NAME"]
    assert settings.API_V1_STR == large_input_values["API_V1_STR"]
    assert settings.LOGGER_CONFIG_PATH == large_input_values["LOGGER_CONFIG_PATH"]

def test_settings_none_values():
    none_values = {
        "API_NAME": None,
        "API_V1_STR": None,
        "LOGGER_CONFIG_PATH": None
    }
    with pytest.raises(ValidationError):
        Settings(**none_values)