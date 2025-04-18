from theory_evaluation.config import Settings
import pytest


def test_settings_default_values():
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    settings = Settings()
    assert settings.API_NAME == expected_api_name
    assert settings.API_V1_STR == expected_api_v1_str
    assert settings.LOGGER_CONFIG_PATH == expected_logger_config_path

def test_settings_custom_values():
    custom_api_name = "custom_api_name"
    custom_api_v1_str = "/custom/api/v1"
    custom_logger_config_path = "/custom/path/logging.yml"
    settings = Settings(API_NAME=custom_api_name, API_V1_STR=custom_api_v1_str, LOGGER_CONFIG_PATH=custom_logger_config_path)
    assert settings.API_NAME == custom_api_name
    assert settings.API_V1_STR == custom_api_v1_str
    assert settings.LOGGER_CONFIG_PATH == custom_logger_config_path

def test_settings_with_empty_strings():
    custom_api_name = ""
    custom_api_v1_str = ""
    custom_logger_config_path = ""
    settings = Settings(API_NAME=custom_api_name, API_V1_STR=custom_api_v1_str, LOGGER_CONFIG_PATH=custom_logger_config_path)
    assert settings.API_NAME == ""
    assert settings.API_V1_STR == ""
    assert settings.LOGGER_CONFIG_PATH == ""

def test_settings_with_unexpected_types():
    custom_api_name = 123
    custom_api_v1_str = True
    custom_logger_config_path = ["invalid", "type"]
    with pytest.raises(ValueError):
        Settings(API_NAME=custom_api_name, API_V1_STR=custom_api_v1_str, LOGGER_CONFIG_PATH=custom_logger_config_path)