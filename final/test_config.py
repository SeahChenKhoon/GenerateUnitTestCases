from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings
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
    assert settings.API_NAME == expected_api_name
    assert settings.API_V1_STR == expected_api_v1_str
    assert settings.LOGGER_CONFIG_PATH == expected_logger_config_path

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        settings = Settings()
    assert settings.API_NAME == custom_values["API_NAME"]
    assert settings.API_V1_STR == custom_values["API_V1_STR"]
    assert settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": "123",
        "API_V1_STR": "",
        "LOGGER_CONFIG_PATH": "456"
    }
    with patch.dict('os.environ', invalid_values):
        settings = Settings()
        assert settings.API_NAME == "123"
        assert settings.API_V1_STR == ""
        assert settings.LOGGER_CONFIG_PATH == "456"