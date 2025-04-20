from theory_evaluation.config import Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    # Arrange & Act
    settings = default_settings

def test_settings_custom_values():
    # Arrange
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }

def test_settings_environment_override(monkeypatch):
    # Arrange
    monkeypatch.setenv("API_NAME", "env_api")
    monkeypatch.setenv("API_V1_STR", "/env/api/v1")
    monkeypatch.setenv("LOGGER_CONFIG_PATH", "/env/path/logging.yml")

def test_settings_invalid_type():
    # Arrange
    invalid_values = {
        "API_NAME": 123,  # Invalid type, should be str
        "API_V1_STR": None,  # Invalid type, should be str
        "LOGGER_CONFIG_PATH": 456  # Invalid type, should be str
    }