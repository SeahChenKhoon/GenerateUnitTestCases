
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def sample_fixture():
    return "sample data"

@pytest.fixture
def another_fixture():
    return {"key": "value"}