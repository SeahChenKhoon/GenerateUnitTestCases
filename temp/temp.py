from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings

def test_global_settings_instance():
    from theory_evaluation.config import SETTINGS
    assert hasattr(SETTINGS, "API_NAME")
    assert SETTINGS.API_NAME == "project_simulation_fastapi"
    assert hasattr(SETTINGS, "API_V1_STR")
    assert SETTINGS.API_V1_STR == "/api/v1"
    assert hasattr(SETTINGS, "LOGGER_CONFIG_PATH")
    assert SETTINGS.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"
