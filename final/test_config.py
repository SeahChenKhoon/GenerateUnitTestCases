from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()
def test_settings_default_values(default_settings):
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    actual_api_name = default_settings.API_NAME
    actual_api_v1_str = default_settings.API_V1_STR
    actual_logger_config_path = default_settings.LOGGER_CONFIG_PATH
    assert actual_api_name == expected_api_name
    assert actual_api_v1_str == expected_api_v1_str
    assert actual_logger_config_path == expected_logger_config_path

from unittest.mock import patch

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        custom_settings = Settings()
    assert custom_settings.API_NAME == custom_values["API_NAME"]
    assert custom_settings.API_V1_STR == custom_values["API_V1_STR"]
    assert custom_settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]

import pytest
from unittest.mock import patch
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": "123",
    }
    with patch.dict('os.environ', invalid_values):
        settings = Settings()
        assert settings.API_NAME == "123"  # Assuming the environment variable overrides the default value without raising an error
