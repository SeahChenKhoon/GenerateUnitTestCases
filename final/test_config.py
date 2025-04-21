from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    api_name = default_settings.API_NAME
    api_v1_str = default_settings.API_V1_STR
    logger_config_path = default_settings.LOGGER_CONFIG_PATH
    assert api_name == "project_simulation_fastapi"
    assert api_v1_str == "/api/v1"
    assert logger_config_path == "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        custom_settings = Settings()
    api_name = custom_settings.API_NAME
    api_v1_str = custom_settings.API_V1_STR
    logger_config_path = custom_settings.LOGGER_CONFIG_PATH
    assert api_name == "custom_api_name"
    assert api_v1_str == "/custom/api/v1"
    assert logger_config_path == "/custom/path/logging.yml"