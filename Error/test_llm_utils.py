
TEST CASE 1 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_prompt_returns_correct_prompt_structure(mock_yaml_load, mock_file):
    agent = "test_agent"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    with patch("builtins.open", mock_open(read_data=mock_prompt_txt)) as mock_prompt_file:
        result = initialise_prompt(agent)
        mock_prompt_file.assert_any_call(prompt_path, "r")
        mock_file.assert_any_call(config_path)
        assert result == "This is a test prompt with placeholders: value1 and value2."

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__ ERROR at setup of test_initialise_prompt_returns_correct_prompt_structure __
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 9
  def test_initialise_prompt_returns_correct_prompt_structure(mock_yaml_load, mock_file):
E       fixture 'mock_yaml_load' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:9
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_returns_correct_prompt_structure
1 error in 0.15s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



from unittest.mock import patch, mock_open
import pytest
import yaml

mock_prompt_txt = "This is a test prompt with placeholders: {$placeholder1} and {$placeholder2}."
mock_config_yaml = """
placeholder1: value1
placeholder2: value2
"""

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value=yaml.safe_load(mock_config_yaml)) as mock_yaml:
        yield mock_yaml

@pytest.fixture
def mock_file():
    with patch("builtins.open", mock_open(read_data=mock_config_yaml)) as mock_file:
        yield mock_file

def test_initialise_prompt_returns_correct_prompt_structure(mock_yaml_load, mock_file):
    agent = "test_agent"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    with patch("builtins.open", mock_open(read_data=mock_prompt_txt)) as mock_prompt_file:
        result = initialise_prompt(agent)
        mock_prompt_file.assert_any_call(prompt_path, "r")
        mock_file.assert_any_call(config_path)
        assert result == "This is a test prompt with placeholders: value1 and value2."

---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
___________ test_initialise_prompt_returns_correct_prompt_structure ___________
temp\temp.py:36: in test_initialise_prompt_returns_correct_prompt_structure
    mock_file.assert_any_call(config_path)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1048: in assert_any_call
    raise AssertionError(
E   AssertionError: open('./theory_evaluation/evaluator/prompts/test_agent/config.yaml') call not found
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_returns_correct_prompt_structure
1 failed in 0.52s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



from unittest.mock import patch, mock_open
import pytest
import yaml

mock_prompt_txt = "This is a test prompt with placeholders: {$placeholder1} and {$placeholder2}."
mock_config_yaml = """
placeholder1: value1
placeholder2: value2
"""

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value=yaml.safe_load(mock_config_yaml)) as mock_yaml:
        yield mock_yaml

@pytest.fixture
def mock_file():
    with patch("builtins.open", mock_open(read_data=mock_config_yaml)) as mock_file:
        yield mock_file

def test_initialise_prompt_returns_correct_prompt_structure(mock_yaml_load, mock_file):
    agent = "test_agent"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    with patch("builtins.open", mock_open(read_data=mock_prompt_txt)) as mock_prompt_file:
        result = initialise_prompt(agent)
        mock_prompt_file.assert_any_call(prompt_path, "r")
        mock_file.assert_any_call(config_path, "r")
        assert result == "This is a test prompt with placeholders: value1 and value2."

---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
___________ test_initialise_prompt_returns_correct_prompt_structure ___________
temp\temp.py:36: in test_initialise_prompt_returns_correct_prompt_structure
    mock_file.assert_any_call(config_path, "r")
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1048: in assert_any_call
    raise AssertionError(
E   AssertionError: open('./theory_evaluation/evaluator/prompts/test_agent/config.yaml', 'r') call not found
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_returns_correct_prompt_structure
1 failed in 0.49s

TEST CASE 3 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_prompt_handles_file_not_found(mock_file):
    agent = "non_existent_agent"
    with pytest.raises(FileNotFoundError):
        initialise_prompt(agent)

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_______ ERROR at setup of test_initialise_prompt_handles_file_not_found _______
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 9
  def test_initialise_prompt_handles_file_not_found(mock_file):
E       fixture 'mock_file' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:9
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_handles_file_not_found
1 error in 0.19s
TEST CASE 3 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_prompt_handles_file_not_found():
    agent = "non_existent_agent"
    with pytest.raises(FileNotFoundError):
        initialise_prompt(agent)

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________ test_initialise_prompt_handles_file_not_found ________________
temp\temp.py:14: in test_initialise_prompt_handles_file_not_found
    with pytest.raises(FileNotFoundError):
E   Failed: DID NOT RAISE <class 'FileNotFoundError'>
---------------------------- Captured stdout call -----------------------------
[Errno 2] No such file or directory: './theory_evaluation/evaluator/prompts/non_existent_agent/config.yaml': No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_handles_file_not_found - Failed: ...
1 failed in 0.29s
TEST CASE 3 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_prompt_handles_file_not_found():
    agent = "non_existent_agent"
    with pytest.raises(FileNotFoundError):
        initialise_prompt(agent)

---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
________________ test_initialise_prompt_handles_file_not_found ________________
temp\temp.py:14: in test_initialise_prompt_handles_file_not_found
    with pytest.raises(FileNotFoundError):
E   Failed: DID NOT RAISE <class 'FileNotFoundError'>
---------------------------- Captured stdout call -----------------------------
[Errno 2] No such file or directory: './theory_evaluation/evaluator/prompts/non_existent_agent/config.yaml': No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_handles_file_not_found - Failed: ...
1 failed in 0.19s

TEST CASE 4 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_settings_handles_file_not_found(mock_file):
    agent = "non_existent_agent"
    with pytest.raises(FileNotFoundError):
        initialise_settings(agent)

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
______ ERROR at setup of test_initialise_settings_handles_file_not_found ______
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 9
  def test_initialise_settings_handles_file_not_found(mock_file):
E       fixture 'mock_file' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:9
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_handles_file_not_found
1 error in 0.26s
TEST CASE 4 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_settings_handles_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", mock_open()) as mocked_file:
        mocked_file.side_effect = FileNotFoundError
        with pytest.raises(FileNotFoundError):
            initialise_settings(agent)

---------------
TEST CASE 4 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________ test_initialise_settings_handles_file_not_found _______________
temp\temp.py:16: in test_initialise_settings_handles_file_not_found
    with pytest.raises(FileNotFoundError):
E   Failed: DID NOT RAISE <class 'FileNotFoundError'>
---------------------------- Captured stdout call -----------------------------
: No configuration path to the llm settings given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_handles_file_not_found - Failed...
1 failed in 0.29s
TEST CASE 4 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_settings_handles_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", mock_open()) as mocked_file:
        mocked_file.side_effect = FileNotFoundError
        with pytest.raises(FileNotFoundError):
            initialise_settings(agent)

---------------
TEST CASE 4 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________ test_initialise_settings_handles_file_not_found _______________
temp\temp.py:16: in test_initialise_settings_handles_file_not_found
    with pytest.raises(FileNotFoundError):
E   Failed: DID NOT RAISE <class 'FileNotFoundError'>
---------------------------- Captured stdout call -----------------------------
: No configuration path to the llm settings given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_handles_file_not_found - Failed...
1 failed in 0.15s

TEST CASE 5 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_prompt_with_missing_placeholders(mock_yaml_load, mock_file):
    agent = "test_agent"
    result = initialise_prompt(agent)
    assert result == "This is a test prompt with placeholders: {$key1} and {$key2}."

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_____ ERROR at setup of test_initialise_prompt_with_missing_placeholders ______
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 9
  def test_initialise_prompt_with_missing_placeholders(mock_yaml_load, mock_file):
E       fixture 'mock_yaml_load' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:9
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_with_missing_placeholders
1 error in 0.20s
TEST CASE 5 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_yaml_load():
    return {"key1": "value1", "key2": "value2"}

@pytest.fixture
def mock_file():
    prompt_content = "This is a test prompt with placeholders: {$key1} and {$key2}."
    return mock_open(read_data=prompt_content)

@patch("builtins.open", new_callable=mock_file)
@patch("yaml.load", return_value=mock_yaml_load())
def test_initialise_prompt_with_missing_placeholders(mock_yaml_load, mock_file):
    agent = "test_agent"
    result = initialise_prompt(agent)
    assert result == "This is a test prompt with placeholders: value1 and value2."

---------------
TEST CASE 5 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
Fixture "mock_yaml_load" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
=========================== short test summary info ===========================
ERROR temp/temp.py - Failed: Fixture "mock_yaml_load" called directly. Fixtur...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.39s
TEST CASE 5 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_yaml_load():
    return {"key1": "value1", "key2": "value2"}

@pytest.fixture
def mock_file():
    prompt_content = "This is a test prompt with placeholders: {$key1} and {$key2}."
    return mock_open(read_data=prompt_content)

@patch("builtins.open", new_callable=lambda: mock_file())
@patch("yaml.load", return_value=mock_yaml_load())
def test_initialise_prompt_with_missing_placeholders(mock_yaml_load, mock_open):
    agent = "test_agent"
    result = initialise_prompt(agent)
    assert result == "This is a test prompt with placeholders: value1 and value2."

---------------
TEST CASE 5 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
Fixture "mock_yaml_load" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
=========================== short test summary info ===========================
ERROR temp/temp.py - Failed: Fixture "mock_yaml_load" called directly. Fixtur...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.50s
