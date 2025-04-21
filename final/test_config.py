from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings

def test_settings_default_values():
    # Arrange
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"

def test_settings_custom_values():
    # Arrange
    custom_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }