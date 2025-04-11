import pytest
from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings

def test_global_settings_instance():
    from theory_evaluation.config import SETTINGS
    assert hasattr(SETTINGS, "API_NAME")
    assert hasattr(SETTINGS, "API_V1_STR")
    assert hasattr(SETTINGS, "LOGGER_CONFIG_PATH")
