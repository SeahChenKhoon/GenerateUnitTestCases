import os
from unittest.mock import patch
import pytest
from theory_evaluation.config import Settings

@pytest.fixture
def settings_fixture():
    return Settings()

def test_settings_default_values(settings_fixture):
    api_name = settings_fixture.API_NAME
    api_v1_str = settings_fixture.API_V1_STR
    logger_config_path = settings_fixture.LOGGER_CONFIG_PATH
    assert api_name == "project_simulation_fastapi"
    assert api_v1_str == "/api/v1"
    assert logger_config_path == "../conf/base/logging.yml"

def test_settings_custom_values():
    with patch.dict(os.environ, {
        'API_NAME': 'custom_api_name',
        'API_V1_STR': '/custom/api/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }):
        settings = Settings()
        assert settings.API_NAME == 'custom_api_name'
        assert settings.API_V1_STR == '/custom/api/v1'
        assert settings.LOGGER_CONFIG_PATH == '/custom/path/logging.yml'

def test_settings_empty_values():
    with patch.dict('os.environ', {
        'API_NAME': '',
        'API_V1_STR': '',
        'LOGGER_CONFIG_PATH': ''
    }):
        settings = Settings()
        assert settings.API_NAME == ''
        assert settings.API_V1_STR == ''
        assert settings.LOGGER_CONFIG_PATH == ''