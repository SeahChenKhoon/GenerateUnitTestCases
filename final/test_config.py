from theory_evaluation.config import Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    settings = default_settings
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    settings = Settings(**custom_values)
    assert settings.API_NAME == "custom_api"
    assert settings.API_V1_STR == "/custom/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": 456,
        "LOGGER_CONFIG_PATH": 789
    }
    with pytest.raises(ValueError):
        Settings(**invalid_values)

def test_settings_partial_override():
    partial_values = {
        "API_NAME": "partial_api"
    }
    settings = Settings(**partial_values)
    assert settings.API_NAME == "partial_api"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"