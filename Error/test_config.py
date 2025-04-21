
TEST CASE 3 Retry 0
---------------
from theory_evaluation.config import Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_invalid_values():
    invalid_values = {
        "API_NAME": None,
        "API_V1_STR": 123,
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', invalid_values):
        with pytest.raises(ValueError):
            Settings()
---------------
from theory_evaluation.config import Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_invalid_values():
    invalid_values = {
        "API_NAME": None,
        "API_V1_STR": 123,
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', invalid_values):
        with pytest.raises(ValueError):
            Settings()
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________________ test_settings_invalid_values _________________________
temp\temp.py:15: in test_settings_invalid_values
    with patch.dict('os.environ', invalid_values):
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1921: in __enter__
    self._patch_dict()
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1946: in _patch_dict
    in_dict.update(values)
<frozen _collections_abc>:987: in update
    ???
<frozen os>:721: in __setitem__
    ???
<frozen os>:781: in check_str
    ???
E   TypeError: str expected, not NoneType
=========================== short test summary info ===========================
FAILED temp/temp.py::test_settings_invalid_values - TypeError: str expected, ...
1 failed in 0.27s
TEST CASE 3 Retry 1
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_invalid_values():
    invalid_values = {
        "API_NAME": "None",
        "API_V1_STR": "123",
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', invalid_values):
        with pytest.raises(ValueError):
            Settings()
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

def test_settings_invalid_values():
    invalid_values = {
        "API_NAME": "None",
        "API_V1_STR": "123",
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', invalid_values):
        with pytest.raises(ValueError):
            Settings()
TEST CASE 3 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________________ test_settings_invalid_values _________________________
temp\temp.py:17: in test_settings_invalid_values
    with pytest.raises(ValueError):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_settings_invalid_values - Failed: DID NOT RAISE <cl...
1 failed in 0.18s
TEST CASE 3 Retry 2
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_invalid_values():
    invalid_values = {
        "API_NAME": None,
        "API_V1_STR": 123,
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', invalid_values):
        with pytest.raises(ValueError):
            Settings()
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest
from unittest.mock import patch

@pytest.fixture
def default_settings():
    return Settings()

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

def test_settings_invalid_values():
    invalid_values = {
        "API_NAME": None,
        "API_V1_STR": 123,
        "LOGGER_CONFIG_PATH": ""
    }
    with patch.dict('os.environ', invalid_values):
        with pytest.raises(ValueError):
            Settings()
TEST CASE 3 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________________ test_settings_invalid_values _________________________
temp\temp.py:21: in test_settings_invalid_values
    with patch.dict('os.environ', invalid_values):
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1921: in __enter__
    self._patch_dict()
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1946: in _patch_dict
    in_dict.update(values)
<frozen _collections_abc>:987: in update
    ???
<frozen os>:721: in __setitem__
    ???
<frozen os>:781: in check_str
    ???
E   TypeError: str expected, not NoneType
=========================== short test summary info ===========================
FAILED temp/temp.py::test_settings_invalid_values - TypeError: str expected, ...
1 failed in 0.29s
