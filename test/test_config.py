import pytest
from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings

def test_settings_default_values():
    settings = Settings()
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_settings = Settings(API_NAME="custom_api", API_V1_STR="/custom/v1", LOGGER_CONFIG_PATH="/custom/path/logging.yml")
    assert custom_settings.API_NAME == "custom_api"
    assert custom_settings.API_V1_STR == "/custom/v1"
    assert custom_settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"