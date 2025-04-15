import os
import re
import yaml

def test_initialise_settings():
    agent = "test_agent"
    llm_settings_content = '{"setting_key": "setting_value"}'
