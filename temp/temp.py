import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch

from unittest.mock import patch


def test_initialise_settings_file_not_found(mock_open_file):
    mock_open_file.side_effect = FileNotFoundError
