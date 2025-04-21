
TEST CASE 2 Retry 0
---------------
import os
import yaml
from theory_evaluation.llm_utils import initialise_settings
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_file_open():
    with patch("builtins.open", mock_open(read_data="key1: value1\nkey2: value2")) as m:
        yield m

@pytest.fixture
def mock_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        yield

def test_initialise_settings(agent, config_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
    m_open = mock_open(read_data=config_content)
    with patch("builtins.open", m_open):
        with patch("os.path.exists", return_value=True):
            result = initialise_settings(agent)
            assert result == expected_output
---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________________ ERROR at setup of test_initialise_settings __________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 17
  def test_initialise_settings(agent, config_content, expected_output):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, mock_file_not_found, mock_file_open, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:17
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings
1 error in 0.19s
TEST CASE 2 Retry 1
---------------
import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_file_open():
    with patch("builtins.open", mock_open(read_data="key1: value1\nkey2: value2")) as m:
        yield m

@pytest.fixture
def mock_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        yield

def test_initialise_settings():
    agent = "test_agent"
    config_content = """
    key1: value1
    key2: value2
    """
    expected_output = {
        "key1": "value1",
        "key2": "value2"
    }
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
    m_open = mock_open(read_data=config_content)
    with patch("builtins.open", m_open):
        with patch("os.path.exists", return_value=True):
            result = initialise_settings(agent)
            assert result == expected_output
---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:6: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
import unittest
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_file_open():
    with patch("builtins.open", mock_open(read_data="key1: value1\nkey2: value2")) as m:
        yield m

@pytest.fixture
def mock_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        yield

class TestInitialiseSettings(unittest.TestCase):
    def test_initialise_settings(self):
        agent = "test_agent"
        config_content = """
        key1: value1
        key2: value2
        """
        expected_output = {
            "key1": "value1",
            "key2": "value2"
        }
        config_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
        m_open = mock_open(read_data=config_content)
        with patch("builtins.open", m_open):
            result = initialise_settings(agent)
            self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:8: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.28s
