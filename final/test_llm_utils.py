import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
@pytest.fixture
def mock_open_files():
    prompt_content = "Hello, {$name}!"
    config_content = "name: World"
    llm_settings_content = "setting: value"
    m_open = mock_open(read_data=prompt_content)
    m_open.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=prompt_content).return_value,
        mock_open(read_data=llm_settings_content).return_value,
    ]
    return m_open