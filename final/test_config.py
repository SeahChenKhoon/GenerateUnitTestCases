from theory_evaluation.config import Settings
import pytest

def test_settings_default_values():
    # Arrange & Act
    settings = Settings()

def test_settings_custom_values():
    # Arrange
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }

def test_settings_invalid_type():
    # Arrange
    invalid_values = {
        "API_NAME": 123,  # Invalid type
        "API_V1_STR": "/api/v1",
        "LOGGER_CONFIG_PATH": "../conf/base/logging.yml"
    }

def test_settings_missing_values():
    # Arrange
    missing_values = {}

def test_settings_environment_variables(monkeypatch):
    # Arrange
    monkeypatch.setenv("API_NAME", "env_api")
    monkeypatch.setenv("API_V1_STR", "/env/v1")
    monkeypatch.setenv("LOGGER_CONFIG_PATH", "/env/path/logging.yml")