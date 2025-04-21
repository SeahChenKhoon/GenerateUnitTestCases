from theory_evaluation.config import Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    settings = default_settings

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }

def test_settings_environment_override(monkeypatch):
    monkeypatch.setenv("API_NAME", "env_api_name")
    monkeypatch.setenv("API_V1_STR", "/env/api/v1")
    monkeypatch.setenv("LOGGER_CONFIG_PATH", "/env/path/logging.yml")