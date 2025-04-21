from pydantic_settings import BaseSettings
import pytest
import os
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_default_values(default_settings):
    assert default_settings.API_NAME == "project_simulation_fastapi"
    assert default_settings.API_V1_STR == "/api/v1"
    assert default_settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_custom_values():
    with patch.dict(os.environ, {
        'API_NAME': 'custom_api',
        'API_V1_STR': '/custom/api/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }):
        custom_settings = Settings()
        assert custom_settings.API_NAME == "custom_api"
        assert custom_settings.API_V1_STR == "/custom/api/v1"
        assert custom_settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_invalid_type():
    with patch.dict(os.environ, {'API_NAME': '123'}):
        settings = Settings()
        assert settings.API_NAME == '123'