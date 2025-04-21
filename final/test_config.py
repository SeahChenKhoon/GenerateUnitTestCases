from theory_evaluation.config import Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    # Arrange
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"

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
        "API_NAME": 123,  # Invalid type, should be str
        "API_V1_STR": None,  # Invalid type, should be str
        "LOGGER_CONFIG_PATH": 456  # Invalid type, should be str
    }