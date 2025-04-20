
TEST CASE 1 Retry 0
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    # Arrange: Create a fixture for the default settings
    return Settings()

@pytest.fixture(scope="function", autouse=True)
def mock_environment_variables():
    # Arrange: Mock environment variables
    with patch.dict('os.environ', {
        'API_NAME': 'env_api_name',
        'API_V1_STR': '/env/api/v1',
        'LOGGER_CONFIG_PATH': '/env/path/logging.yml'
    }):
        yield

def test_settings_default_values(default_settings):
    settings = default_settings
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_______________ ERROR at setup of test_settings_default_values ________________
temp\temp.py:13: in mock_environment_variables
    with patch.dict('os.environ', {
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_settings_default_values - NameError: name 'patch' is...
1 error in 0.20s
TEST CASE 1 Retry 1
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    # Arrange: Create a fixture for the default settings
    return Settings()

@pytest.fixture(scope="function", autouse=True)
def mock_environment_variables():
    # Arrange: Mock environment variables
    with patch.dict('os.environ', {
        'API_NAME': 'env_api_name',
        'API_V1_STR': '/env/api/v1',
        'LOGGER_CONFIG_PATH': '/env/path/logging.yml'
    }):
        yield

from unittest.mock import patch

def test_settings_default_values(default_settings):
    settings = default_settings
    assert settings.API_NAME == "project_simulation_fastapi"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________________ test_settings_default_values _________________________
temp\temp.py:24: in test_settings_default_values
    assert settings.API_NAME == "project_simulation_fastapi"
E   AssertionError: assert 'env_api_name' == 'project_simulation_fastapi'
E     
E     - project_simulation_fastapi
E     + env_api_name
=========================== short test summary info ===========================
FAILED temp/temp.py::test_settings_default_values - AssertionError: assert 'e...
1 failed in 0.33s
TEST CASE 1 Retry 2
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings():
    # Arrange: Create a fixture for the default settings
    return Settings()

@pytest.fixture(scope="function", autouse=True)
def mock_environment_variables():
    # Arrange: Mock environment variables
    with patch.dict('os.environ', {
        'API_NAME': 'env_api_name',
        'API_V1_STR': '/env/api/v1',
        'LOGGER_CONFIG_PATH': '/env/path/logging.yml'
    }):
        yield

from unittest.mock import patch

def test_settings_default_values():
    with patch('temp.Settings', return_value=Settings(API_NAME="project_simulation_fastapi")):
        settings = Settings()
        assert settings.API_NAME == "project_simulation_fastapi"
        assert settings.API_V1_STR == "/api/v1"
        assert settings.LOGGER_CONFIG_PATH == "../conf/base/logging.yml"

---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________________ test_settings_default_values _________________________
temp\temp.py:26: in test_settings_default_values
    assert settings.API_V1_STR == "/api/v1"
E   AssertionError: assert '/env/api/v1' == '/api/v1'
E     
E     - /api/v1
E     + /env/api/v1
E     ? ++++
=========================== short test summary info ===========================
FAILED temp/temp.py::test_settings_default_values - AssertionError: assert '/...
1 failed in 0.24s
