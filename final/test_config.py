from theory_evaluation.config import SETTINGS, Settings
import pytest
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_default_values():
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }

@pytest.mark.parametrize("env_var, value", [
    ("API_NAME", "custom_api_name"),
    ("API_V1_STR", "/custom/api/v1"),
    ("LOGGER_CONFIG_PATH", "/custom/path/logging.yml"),
])
def test_settings_edge_cases(monkeypatch, env_var, value):
    monkeypatch.setenv(env_var, value)
    settings = Settings()
    assert getattr(settings, env_var) == value