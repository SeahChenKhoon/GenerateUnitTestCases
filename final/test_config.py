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