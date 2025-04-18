
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings

@pytest.fixture
def sample_fixture():
    # Setup code
    data = {"key": "value"}
    yield data
    # Teardown code

@pytest.fixture
def another_fixture():
    # Setup code
    resource = open("file.txt", "w")
    yield resource
    # Teardown code
    resource.close()