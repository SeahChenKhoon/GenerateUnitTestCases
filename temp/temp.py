import pytest
from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings

def test_settings_attributes():
    assert hasattr(Settings, 'API_NAME')
    assert hasattr(Settings, 'API_V1_STR')
    assert hasattr(Settings, 'LOGGER_CONFIG_PATH')
