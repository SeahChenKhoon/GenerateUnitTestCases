
TEST CASE 1 Retry 0
---------------
import yaml
import pytest

def test_initialise_prompt(agent, config_data, prompt_data, expected_output):
    config_yaml = yaml.dump(config_data)
    mock_files = {
        f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml": config_yaml,
        f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt": prompt_data
    }
---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________________ ERROR at setup of test_initialise_prompt ___________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 4
  def test_initialise_prompt(agent, config_data, prompt_data, expected_output):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:4
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt
1 error in 0.13s
TEST CASE 1 Retry 1
---------------
import yaml
from your_module import initialise_prompt
import pytest

@pytest.mark.parametrize("agent, config_data, prompt_data, expected_output", [
    ("agent1", {"key1": "value1"}, "Hello {$key1}", "Hello value1"),
    ("agent2", {"key2": "value2"}, "Welcome {$key2}", "Welcome value2"),
])
def test_initialise_prompt(agent, config_data, prompt_data, expected_output, monkeypatch):
    config_yaml = yaml.dump(config_data)
    mock_files = {
        f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml": config_yaml,
        f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt": prompt_data
    }

    def mock_open(file, mode='r', *args, **kwargs):
        if file in mock_files:
            return mock_files[file]
        else:
            raise FileNotFoundError(f"No such file or directory: '{file}'")

    monkeypatch.setattr("builtins.open", mock_open)

    result = initialise_prompt(agent)
    assert result == expected_output
---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:2: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s
TEST CASE 1 Retry 2
---------------
import yaml
import pytest
from io import StringIO
from unittest.mock import patch
from your_module import initialise_prompt

@pytest.mark.parametrize("agent, config_data, prompt_data, expected_output", [
    ("agent1", {"key1": "value1"}, "Hello {$key1}", "Hello value1"),
    ("agent2", {"key2": "value2"}, "Welcome {$key2}", "Welcome value2"),
])
def test_initialise_prompt(agent, config_data, prompt_data, expected_output):
    config_yaml = yaml.dump(config_data)
    mock_files = {
        f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml": config_yaml,
        f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt": prompt_data
    }

    def mock_file_open(file, mode='r', *args, **kwargs):
        if file in mock_files:
            return StringIO(mock_files[file])
        else:
            raise FileNotFoundError(f"No such file or directory: '{file}'")

    with patch("builtins.open", mock_file_open):
        result = initialise_prompt(agent)
        assert result == expected_output
---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:5: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.28s

TEST CASE 3 Retry 0
---------------
import yaml
from theory_evaluation.llm_utils import initialise_settings

def test_initialise_settings(agent, settings_data, expected_output):
    settings_yaml = yaml.dump(settings_data)
    mock_files = {
        f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml": settings_yaml
    }
---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________________ ERROR at setup of test_initialise_settings __________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 4
  def test_initialise_settings(agent, settings_data, expected_output):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:4
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings
1 error in 0.13s
TEST CASE 3 Retry 1
---------------
import yaml
import pytest

def test_initialise_settings(monkeypatch):
    agent = "test_agent"
    settings_data = {
        "setting1": "value1",
        "setting2": "value2"
    }
    expected_output = settings_data

    settings_yaml = yaml.dump(settings_data)
    mock_files = {
        f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml": settings_yaml
    }

    def mock_open(file, *args, **kwargs):
        if file in mock_files:
            return mock_files[file]
        else:
            raise FileNotFoundError(f"No such file: '{file}'")

    monkeypatch.setattr("builtins.open", lambda file, *args, **kwargs: mock_open(file, *args, **kwargs))

    from your_module import initialise_settings

    result = initialise_settings(agent)
    assert result == expected_output
---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
__________________________ test_initialise_settings ___________________________
temp\temp.py:25: in test_initialise_settings
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings - ModuleNotFoundError: No modul...
1 failed in 0.20s
TEST CASE 3 Retry 2
---------------
import yaml
from theory_evaluation.llm_utils import initialise_settings
import pytest

def test_initialise_settings(monkeypatch):
    agent = "test_agent"
    settings_data = {
        "setting1": "value1",
        "setting2": "value2"
    }
    expected_output = settings_data

    settings_yaml = yaml.dump(settings_data)
    mock_files = {
        f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml": settings_yaml
    }

    def mock_open(file, *args, **kwargs):
        if file in mock_files:
            return mock_files[file]
        else:
            raise FileNotFoundError(f"No such file: '{file}'")

    monkeypatch.setattr("builtins.open", lambda file, *args, **kwargs: mock_open(file, *args, **kwargs))

    result = initialise_settings(agent)
    assert result == expected_output
---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
__________________________ test_initialise_settings ___________________________
temp\temp.py:27: in test_initialise_settings
    assert result == expected_output
E   AssertionError: assert None == {'setting1': 'value1', 'setting2': 'value2'}
---------------------------- Captured stdout call -----------------------------
'str' object does not support the context manager protocol: No configuration path to the llm settings given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings - AssertionError: assert None =...
1 failed in 0.22s
