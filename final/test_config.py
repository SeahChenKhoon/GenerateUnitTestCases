from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest


from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest


def test_settings_default_values():
    settings = Settings()
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
    assert settings.API_NAME == custom_values["API_NAME"]
    assert settings.API_V1_STR == custom_values["API_V1_STR"]
    assert settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]

import pytest
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_invalid_values():
    with pytest.raises(ValueError):
        Settings(API_NAME=123)  # Invalid type for API_NAME
    with pytest.raises(ValueError):
        Settings(API_V1_STR=[])  # Invalid type for API_V1_STR
    with pytest.raises(ValueError):
        Settings(LOGGER_CONFIG_PATH=None)  # Invalid type for LOGGER_CONFIG_PATH
