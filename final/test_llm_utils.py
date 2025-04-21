import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Mock environment variables or other global states if needed
    yield
    # Teardown: Clean up any changes to global states or environment variables
    pass
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Mock environment variables or other global states if needed
    yield
    # Teardown: Clean up any changes to global states or environment variables
    pass