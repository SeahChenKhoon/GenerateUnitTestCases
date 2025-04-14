from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings

def test_settings_custom_values():
    settings = Settings(API_NAME="custom_api", API_V1_STR="/custom/v1", LOGGER_CONFIG_PATH="/custom/path/logging.yml")
    assert settings.API_NAME == "custom_api"
    assert settings.API_V1_STR == "/custom/v1"
    assert settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"
