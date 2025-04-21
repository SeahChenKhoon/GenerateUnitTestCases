from theory_evaluation.config import Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

@pytest.fixture
def mock_env_vars():
    with patch.dict('os.environ', {'API_NAME': 'env_api', 'API_V1_STR': '/env/v1', 'LOGGER_CONFIG_PATH': '/env/path/logging.yml'}):
        yield

def test_settings_default_values(default_settings):
    assert default_settings.API_NAME == "project_simulation_fastapi"
    assert default_settings.API_V1_STR == "/api/v1"
    assert default_settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_custom_values():
    custom_settings = Settings(API_NAME="custom_api", API_V1_STR="/custom/v1", LOGGER_CONFIG_PATH="/custom/path/logging.yml")
    assert custom_settings.API_NAME == "custom_api"
    assert custom_settings.API_V1_STR == "/custom/v1"
    assert custom_settings.LOGGER_CONFIG_PATH == "/custom/path/logging.yml"

def test_settings_invalid_type():
    with pytest.raises(ValueError):
        Settings(API_NAME=123, API_V1_STR=456, LOGGER_CONFIG_PATH=789)

def test_settings_none_values():
    with pytest.raises(ValueError):
        Settings(API_NAME=None, API_V1_STR=None, LOGGER_CONFIG_PATH=None)

def test_settings_env_vars():
    with patch.dict('os.environ', {'API_NAME': 'env_api', 'API_V1_STR': '/env/v1', 'LOGGER_CONFIG_PATH': '/env/path/logging.yml'}):
        env_settings = Settings()
        assert env_settings.API_NAME == "env_api"
        assert env_settings.API_V1_STR == "/env/v1"
        assert env_settings.LOGGER_CONFIG_PATH == "/env/path/logging.yml"