from pydantic_settings import BaseSettings
import pytest

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

@pytest.fixture
def default_settings():
    return {
        'API_NAME': "project_simulation_fastapi",
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }

def test_settings_default_values():
    settings = Settings()
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

@pytest.mark.parametrize("field, value", [
    ('API_NAME', "new_api_name"),
    ('API_V1_STR', "/new/api/v1"),
    ('LOGGER_CONFIG_PATH', "/new/path/logging.yml")
])
def test_settings_custom_values(field, value):
    custom_values = {field: value}
    settings = Settings(**custom_values)
    assert getattr(settings, field) == value