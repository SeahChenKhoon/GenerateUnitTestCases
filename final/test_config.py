from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import os
from unittest.mock import patch

def test_settings_default_values():
    settings = Settings()
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_override_values():
    with patch.dict('os.environ', {
        'API_NAME': 'custom_api_name',
        'API_V1_STR': '/custom/api/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }):
        settings = Settings()
        assert settings.API_NAME == "custom_api_name"
        assert settings.API_V1_STR == "/custom/api/v1"
        assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_partial_override():
    env_vars = {
        'API_NAME': 'custom_api_name',
        'API_V1_STR': '/custom/api/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }
    expected_values = {
        'API_NAME': 'custom_api_name',
        'API_V1_STR': '/custom/api/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }
    
    with patch.dict(os.environ, env_vars):
        settings = Settings()
        assert settings.API_NAME == expected_values['API_NAME']
        assert settings.API_V1_STR == expected_values['API_V1_STR']
        assert settings.LOGGER_CONFIG_PATH == expected_values['LOGGER_CONFIG_PATH']