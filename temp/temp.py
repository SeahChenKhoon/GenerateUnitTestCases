import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch, mock_open

from unittest.mock import patch, mock_open

from unittest.mock import patch

from unittest.mock import patch


def test_initialise_settings_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("test_agent")
        assert result is None
