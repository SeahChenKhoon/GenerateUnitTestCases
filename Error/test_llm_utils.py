
TEST CASE 1 Retry 0
---------------
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

def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________________ ERROR at setup of test_initialise_prompt ___________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 14
  def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, setup_and_teardown, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:14
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt
1 error in 0.09s
TEST CASE 1 Retry 1
---------------
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
import pytest
import yaml
from unittest.mock import mock_open, patch

from your_module import initialise_prompt  # Replace with the actual module name

@pytest.fixture
def mock_filesystem():
    config_content = """
    key1: value1
    key2: value2
    """
    prompt_content = "This is a prompt with a {$key1} and {$key2}."
    expected_output = "This is a prompt with a value1 and value2."
    return config_content, prompt_content, expected_output

def test_initialise_prompt(mock_filesystem):
    agent = "test_agent"
    config_content, prompt_content, expected_output = mock_filesystem

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
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
temp\temp.py:19: in <module>
    from your_module import initialise_prompt  # Replace with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s
TEST CASE 1 Retry 2
---------------
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
import pytest
import yaml
from unittest.mock import mock_open, patch

from theory_evaluation.evaluator.prompts import initialise_prompt

@pytest.fixture
def mock_filesystem():
    config_content = """
    key1: value1
    key2: value2
    """
    prompt_content = "This is a prompt with a {$key1} and {$key2}."
    expected_output = "This is a prompt with a value1 and value2."
    return config_content, prompt_content, expected_output

def test_initialise_prompt(mock_filesystem):
    agent = "test_agent"
    config_content, prompt_content, expected_output = mock_filesystem

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
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
temp\temp.py:19: in <module>
    from theory_evaluation.evaluator.prompts import initialise_prompt
E   ModuleNotFoundError: No module named 'theory_evaluation.evaluator'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.32s

TEST CASE 2 Retry 0
---------------
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

def test_initialise_settings(agent, settings_content, expected_output):
    settings_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________________ ERROR at setup of test_initialise_settings __________________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 14
  def test_initialise_settings(agent, settings_content, expected_output):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, setup_and_teardown, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:14
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings
1 error in 0.12s
TEST CASE 2 Retry 1
---------------
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

import pytest
import yaml
from unittest.mock import mock_open, patch
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_yaml_content():
    return """
    key1: value1
    key2: value2
    """

def test_initialise_settings(mock_yaml_content):
    agent = "test_agent"
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    settings_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"

    with patch("builtins.open", mock_open(read_data=mock_yaml_content)):
        with patch("yaml.safe_load", return_value=expected_output):
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
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:17: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.30s
TEST CASE 2 Retry 2
---------------
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

import pytest
import yaml
from unittest.mock import mock_open, patch
from theory_evaluation.evaluator.prompts import initialise_settings  # Adjusted import path

@pytest.fixture
def mock_yaml_content():
    return """
    key1: value1
    key2: value2
    """

def test_initialise_settings(mock_yaml_content):
    agent = "test_agent"
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    settings_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"

    with patch("builtins.open", mock_open(read_data=mock_yaml_content)):
        with patch("yaml.safe_load", return_value=expected_output):
            result = initialise_settings(agent)
            assert result == expected_output

---------------
TEST CASE 2 Retry 2 - Result - Failed
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
temp\temp.py:17: in <module>
    from theory_evaluation.evaluator.prompts import initialise_settings  # Adjusted import path
E   ModuleNotFoundError: No module named 'theory_evaluation.evaluator'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.37s

TEST CASE 3 Retry 0
---------------
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

def test_initialise_prompt_exception():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
______________________ test_initialise_prompt_exception _______________________
temp\temp.py:15: in test_initialise_prompt_exception
    with patch("builtins.open", side_effect=FileNotFoundError):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_exception - NameError: name 'patc...
1 failed in 0.22s
TEST CASE 3 Retry 1
---------------
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

from unittest.mock import patch
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt_exception():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None

---------------
TEST CASE 3 Retry 1 - Result - Failed
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
temp\temp.py:15: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.32s
TEST CASE 3 Retry 2
---------------
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

from unittest.mock import patch
from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_prompt_exception():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt("non_existent_agent")
        assert result is None

---------------
TEST CASE 3 Retry 2 - Result - Failed
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
temp\temp.py:15: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.16s

TEST CASE 4 Retry 0
---------------
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

def test_initialise_settings_exception():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_____________________ test_initialise_settings_exception ______________________
temp\temp.py:15: in test_initialise_settings_exception
    with patch("builtins.open", side_effect=FileNotFoundError):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_exception - NameError: name 'pa...
1 failed in 0.17s
TEST CASE 4 Retry 1
---------------
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

from unittest.mock import patch
from your_module import initialise_settings

def test_initialise_settings_exception():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None

---------------
TEST CASE 4 Retry 1 - Result - Failed
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
temp\temp.py:15: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.37s
TEST CASE 4 Retry 2
---------------
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

from unittest.mock import patch
from your_module import initialise_settings

def test_initialise_settings_exception():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
        assert result is None

---------------
TEST CASE 4 Retry 2 - Result - Failed
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
temp\temp.py:15: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.23s
