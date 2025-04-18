from theory_evaluation.config import Settings
import pytest

def test_settings_default_values():
    # Arrange & Act
    settings = Settings()

def test_settings_custom_values():
    # Arrange
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }

def test_settings_environment_override(monkeypatch):
    # Arrange
    monkeypatch.setenv("API_NAME", "env_api_name")
    monkeypatch.setenv("API_V1_STR", "/env/api/v1")
    monkeypatch.setenv("LOGGER_CONFIG_PATH", "/env/path/logging.yml")