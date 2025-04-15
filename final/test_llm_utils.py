import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch

from unittest.mock import mock_open


@patch("theory_evaluation.llm_utils.open", new_callable=mock_open)
@patch("theory_evaluation.llm_utils.yaml.load")
def test_initialise_prompt(mock_yaml_load, mock_open_files):
    mock_yaml_load.return_value = {"name": "World"}
    mock_open_files.side_effect = [
        mock_open(read_data="name: World").return_value,
        mock_open(read_data="Hello, {$name}!").return_value
    ]

@patch("theory_evaluation.llm_utils.open", new_callable=mock_open)
@patch("theory_evaluation.llm_utils.yaml.safe_load")
def test_initialise_settings(mock_yaml_safe_load, mock_open_files):
    mock_yaml_safe_load.return_value = {"setting1": "value1", "setting2": "value2"}
