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
    custom_values = {
        'API_NAME': 'custom_api',
        'API_V1_STR': '/custom/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }
    settings = Settings(**custom_values)
    assert settings.API_NAME == custom_values['API_NAME']
    assert settings.API_V1_STR == custom_values['API_V1_STR']
    assert settings.LOGGER_CONFIG_PATH == custom_values['LOGGER_CONFIG_PATH']

def test_settings_invalid_type():
    invalid_values = {
        'API_NAME': 123,
        'API_V1_STR': None,
        'LOGGER_CONFIG_PATH': []
    }
    with pytest.raises(ValueError):
        Settings(**invalid_values)