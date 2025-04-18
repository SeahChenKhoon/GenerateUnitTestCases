from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_initialization_with_defaults(default_settings):
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    settings_instance = default_settings
    assert settings_instance.API_NAME == expected_api_name
    assert settings_instance.API_V1_STR == expected_api_v1_str
    assert settings_instance.LOGGER_CONFIG_PATH == expected_logger_config_path

def test_settings_initialization_with_custom_values():
    custom_values = {
        "API_NAME": "custom_api_name",
        "API_V1_STR": "/custom/api/v1",
        "LOGGER_CONFIG_PATH": "/custom/path/logging.yml"
    }
    settings_instance = Settings(**custom_values)
    assert settings_instance.API_NAME == custom_values["API_NAME"]
    assert settings_instance.API_V1_STR == custom_values["API_V1_STR"]
    assert settings_instance.LOGGER_CONFIG_PATH == custom_values["LOGGER_CONFIG_PATH"]

def test_settings_initialization_with_empty_strings():
    empty_values = {
        "API_NAME": "",
        "API_V1_STR": "",
        "LOGGER_CONFIG_PATH": ""
    }
    settings_instance = Settings(**empty_values)
    assert settings_instance.API_NAME == ""
    assert settings_instance.API_V1_STR == ""
    assert settings_instance.LOGGER_CONFIG_PATH == ""

def test_settings_initialization_with_invalid_types():
    invalid_values = {
        "API_NAME": 123,
        "API_V1_STR": 456,
        "LOGGER_CONFIG_PATH": 789
    }
    with pytest.raises(ValueError):
        Settings(**invalid_values)

def test_settings_singleton_instance():
    expected_instance = Settings()
    singleton_instance = SETTINGS
    assert singleton_instance.API_NAME == expected_instance.API_NAME
    assert singleton_instance.API_V1_STR == expected_instance.API_V1_STR
    assert singleton_instance.LOGGER_CONFIG_PATH == expected_instance.LOGGER_CONFIG_PATH