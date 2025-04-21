from theory_evaluation.config import Settings
import pytest

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_default_values(default_settings):
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"
    assert default_settings.API_NAME == expected_api_name
    assert default_settings.API_V1_STR == expected_api_v1_str
    assert default_settings.LOGGER_CONFIG_PATH == expected_logger_config_path

def test_settings_custom_values():
    custom_api_name = "custom_api"
    custom_api_v1_str = "/custom/api/v1"
    custom_logger_config_path = "/custom/path/logging.yml"
    custom_settings = Settings(
        API_NAME=custom_api_name,
        API_V1_STR=custom_api_v1_str,
        LOGGER_CONFIG_PATH=custom_logger_config_path
    )
    assert custom_settings.API_NAME == custom_api_name
    assert custom_settings.API_V1_STR == custom_api_v1_str
    assert custom_settings.LOGGER_CONFIG_PATH == custom_logger_config_path

def test_settings_invalid_type():
    invalid_api_name = 123
    with pytest.raises(ValueError):
        Settings(API_NAME=invalid_api_name)

def test_settings_environment_variable_override(monkeypatch):
    monkeypatch.setenv("API_NAME", "env_api_name")
    settings_with_env_override = Settings()
    assert settings_with_env_override.API_NAME == "env_api_name"