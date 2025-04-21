from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from pydantic import ValidationError

def test_settings_default_values():
    # Arrange & Act
    settings = Settings()

def test_settings_override_values():
    # Arrange
    override_values = {
        'API_NAME': 'custom_api_name',
        'API_V1_STR': '/custom/api/v1',
        'LOGGER_CONFIG_PATH': '/custom/path/logging.yml'
    }

@pytest.mark.parametrize("field, value", [
    ("API_NAME", 123),  # Invalid type
    ("API_V1_STR", 456),  # Invalid type
    ("LOGGER_CONFIG_PATH", 789)  # Invalid type
])
def test_settings_invalid_values(field, value):
    # Arrange
    override_values = {field: value}
    
    # Act & Assert
    with pytest.raises(ValidationError):
        Settings(**override_values)