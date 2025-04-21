
TEST CASE 3 Retry 0
---------------
from theory_evaluation.config import SETTINGS

def test_settings_edge_cases(env_var, value):
    # Arrange
    custom_values = {env_var: value}
---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________________ ERROR at setup of test_settings_edge_cases __________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 3
  def test_settings_edge_cases(env_var, value):
E       fixture 'env_var' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:3
=========================== short test summary info ===========================
ERROR temp/temp.py::test_settings_edge_cases
1 error in 0.20s
TEST CASE 3 Retry 1
---------------
from theory_evaluation.config import SETTINGS, Settings
import pytest

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

@pytest.mark.parametrize("env_var, value", [
    ("API_NAME", "custom_api_name"),
    ("API_V1_STR", "/custom/api/v1"),
    ("LOGGER_CONFIG_PATH", "/custom/path/logging.yml"),
])
def test_settings_edge_cases(monkeypatch, env_var, value):
    monkeypatch.setenv(env_var, value)
    settings = Settings()
    assert getattr(settings, env_var) == value
---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:4: in <module>
    class Settings(BaseSettings):
E   NameError: name 'BaseSettings' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'BaseSettings' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.34s
TEST CASE 3 Retry 2
---------------
from theory_evaluation.config import SETTINGS, Settings
import pytest

class Settings(BaseSettings):
    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"

@pytest.mark.parametrize("env_var, value", [
    ("API_NAME", "custom_api_name"),
    ("API_V1_STR", "/custom/api/v1"),
    ("LOGGER_CONFIG_PATH", "/custom/path/logging.yml"),
])
def test_settings_edge_cases(monkeypatch, env_var, value):
    monkeypatch.setenv(env_var, value)
    settings = Settings()
    assert getattr(settings, env_var) == value
---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:4: in <module>
    class Settings(BaseSettings):
E   NameError: name 'BaseSettings' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'BaseSettings' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s
