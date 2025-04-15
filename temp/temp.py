from unittest.mock import patch

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None