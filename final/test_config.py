from pydantic_settings import BaseSettings
from theory_evaluation.config import Settings
import pytest


def test_settings_default_values():
    # Arrange
    expected_api_name = "project_simulation_fastapi"
    expected_api_v1_str = "/api/v1"
    expected_logger_config_path = "../conf/base/logging.yml"

def test_settings_custom_values():
    # Arrange
    custom_api_name = "custom_api"
    custom_api_v1_str = "/custom/v1"
    custom_logger_config_path = "/custom/path/logging.yml"

def test_settings_empty_string_values():
    # Arrange
    empty_api_name = ""
    empty_api_v1_str = ""
    empty_logger_config_path = ""

def test_settings_none_values():
    # Arrange
    none_api_name = None
    none_api_v1_str = None
    none_logger_config_path = None

def test_settings_invalid_type_values():
    # Arrange
    invalid_api_name = 123
    invalid_api_v1_str = 456
    invalid_logger_config_path = 789