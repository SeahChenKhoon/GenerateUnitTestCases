
TEST CASE 3 Retry 0
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings(self):
    return {
        'API_NAME': "project_simulation_fastapi",
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }

def test_settings_invalid_type(self):
    # Arrange
    invalid_values = {
        'API_NAME': 123,  # Invalid type
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
________________ ERROR at setup of test_settings_invalid_type _________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 13
  def test_settings_invalid_type(self):
E       fixture 'self' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, default_settings, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:13
=========================== short test summary info ===========================
ERROR temp/temp.py::test_settings_invalid_type
1 error in 0.39s
TEST CASE 3 Retry 1
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings(self):
    return {
        'API_NAME': "project_simulation_fastapi",
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }

import pytest
from pydantic_settings import ValidationError
from your_module import Settings  # Replace 'your_module' with the actual module name

def test_settings_invalid_type():
    # Arrange
    invalid_values = {
        'API_NAME': 123,  # Invalid type
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }
    
    # Act & Assert
    with pytest.raises(ValidationError):
        Settings(**invalid_values)

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:14: in <module>
    from pydantic_settings import ValidationError
E   ImportError: cannot import name 'ValidationError' from 'pydantic_settings' (C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pydantic_settings\__init__.py)
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.56s
TEST CASE 3 Retry 2
---------------
from pydantic_settings import BaseSettings
from theory_evaluation.config import SETTINGS, Settings
import pytest

@pytest.fixture
def default_settings(self):
    return {
        'API_NAME': "project_simulation_fastapi",
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }

import pytest
from pydantic import ValidationError
from your_module import Settings  # Replace 'your_module' with the actual module name

def test_settings_invalid_type():
    # Arrange
    invalid_values = {
        'API_NAME': 123,  # Invalid type
        'API_V1_STR': "/api/v1",
        'LOGGER_CONFIG_PATH': "../conf/base/logging.yml"
    }
    
    # Act & Assert
    with pytest.raises(ValidationError):
        Settings(**invalid_values)

---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:15: in <module>
    from your_module import Settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.48s
