import pytest
from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings

def test_settings_default_values():
    settings = Settings()
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

def test_settings_instance():
    assert isinstance(Settings(), BaseSettings)