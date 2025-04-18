from theory_evaluation.config import Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def settings_fixture():
    return Settings()

def test_settings_default_values(settings_fixture):
    settings = settings_fixture
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        settings = Settings()
    assert settings.API_NAME == "custom_api_name"
    assert settings.API_V1_STR == "/custom/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_empty_values():
    empty_values = {
        "API_NAME": "",
        "API_V1_STR": "",
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', empty_values):
        settings = Settings()
    assert settings.API_NAME == ""
    assert settings.API_V1_STR == ""
    assert settings.LOGGER_CONFIG_PATH == ""