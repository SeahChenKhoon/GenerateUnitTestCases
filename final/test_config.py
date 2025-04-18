from pydantic_settings import BaseSettings
import pytest
from pydantic import ValidationError

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

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
    assert settings.API_NAME == "custom_api"
    assert settings.API_V1_STR == "/custom/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_invalid_type():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": "/api/v1",
        "LOGGER_CONFIG_PATH": "../conf/base/logging.yml"
    }
    with pytest.raises(ValidationError):
        Settings(**invalid_values)

def test_settings_missing_values():
    missing_values = {}
    settings = Settings(**missing_values)
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_env_variables(monkeypatch):
    monkeypatch.setenv("API_NAME", "env_api")
    monkeypatch.setenv("API_V1_STR", "/env/api/v1")
    monkeypatch.setenv("LOGGER_CONFIG_PATH", "/env/path/logging.yml")
    settings = Settings()
    assert settings.API_NAME == "env_api"
    assert settings.API_V1_STR == "/env/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "/env/path/logging.yml"