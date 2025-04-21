from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

from unittest.mock import patch
from your_module import Settings  # Replace 'your_module' with the actual module name

def test_settings_custom_values():
    custom_values = {
        "API_NAME": "custom_api",
        "API_V1_STR": "/custom/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    with patch.dict('os.environ', custom_values):
        custom_settings = Settings()
    assert custom_settings.API_NAME == custom_values["API_NAME"]
    assert custom_settings.API_V1_STR == custom_values["API_V1_STR"]
    assert custom_settings.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]
