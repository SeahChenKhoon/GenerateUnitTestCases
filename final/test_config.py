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
    custom_api_name = "custom_api"
    custom_api_v1_str = "/custom/api/v1"
    custom_logger_config_path = "/custom/path/logging.yml"

def test_settings_invalid_type():
    # Arrange
    invalid_api_name = 123  # Invalid type, should be a string