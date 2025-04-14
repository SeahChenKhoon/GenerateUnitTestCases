from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings
from theory_evaluation import models


def test_settings_instance():
    assert isinstance(Settings(), BaseSettings)
