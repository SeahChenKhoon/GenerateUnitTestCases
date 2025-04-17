from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings
import pytest


from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings
import pytest


def test_settings_default_values():
    settings = Settings()
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    settings = Settings(**custom_values)
    assert settings.API_NAME == "custom_api"
    assert settings.API_V1_STR == "/custom/v1"
    assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

import pytest
from pydantic import ValidationError
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": "/api/v1",
        "LOGGER_CONFIG_PATH": "../conf/base/logging.yml"
    }
    with pytest.raises(ValidationError):
        Settings(**invalid_values)

import pytest
from pydantic import ValidationError
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_missing_values():
    missing_values = {
        "API_NAME": None,
        "API_V1_STR": "/api/v1",
        "LOGGER_CONFIG_PATH": "../conf/base/logging.yml"
    }
    with pytest.raises(ValidationError):
        Settings(**missing_values)

def test_settings_large_input():
    large_api_name = "a" * 1000
    settings = Settings(API_NAME=large_api_name)
    assert settings.API_NAME == large_api_name

from unittest.mock import patch

def test_settings_environment_variable_override():
    with patch.dict('os.environ', {'API_NAME': 'env_api_name'}):
        settings = Settings()
    assert settings.API_NAME == 'env_api_name'
