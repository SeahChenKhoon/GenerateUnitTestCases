import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest
@pytest.fixture
def mock_open_files():
    prompt_content = "This is a {$placeholder} test."
    config_content = '{"placeholder": "sample"}'
    llm_settings_content = '{"setting": "value"}'
    with patch("theory_evaluation.llm_utils.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
        with patch("theory_evaluation.llm_utils.open", mock_open(read_data=config_content)) as mock_config_file:
            with patch("theory_evaluation.llm_utils.open", mock_open(read_data=llm_settings_content)) as mock_llm_file:
                yield mock_prompt_file, mock_config_file, mock_llm_file