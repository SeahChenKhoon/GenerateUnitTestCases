from theory_evaluation.config import Settings
import pytest
from pydantic import ValidationError

@pytest.fixture
def valid_settings():
    return {
        "API_NAME": "project_simulation_fastapi",
        "API_V1_STR": "/api/v1",
        "LOGGER_CONFIG_PATH": "../conf/base/logging.yml"
    }

def test_settings_initialization_with_defaults(valid_settings):
    settings = Settings()
    assert settings.API_NAME == valid_settings["API_NAME"]
    assert settings.API_V1_STR == valid_settings["API_V1_STR"]
    assert settings.LOGGER_CONFIG_PATH == valid_settings["LOGGER_CONFIG_PATH"]

def test_settings_initialization_with_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    settings = Settings(**custom_values)
    assert settings.API_NAME == custom_values["API_NAME"]
    assert settings.API_V1_STR == custom_values["API_V1_STR"]
    assert settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]

def test_settings_initialization_with_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": "/api/v1",
        "LOGGER_CONFIG_PATH": "../conf/base/logging.yml"
    }
    with pytest.raises(ValidationError):
        Settings(**invalid_values)

def test_settings_initialization_with_none_values():
    none_values = {
        "API_NAME": None,
        "API_V1_STR": None,
        "LOGGER_CONFIG_PATH": None
    }
    settings = Settings(**{k: v for k, v in none_values.items() if v is not None})
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"