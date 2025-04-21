
TEST CASE 1 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

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
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 17
  def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, mock_open_fixture, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory, yaml_load_fixture
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:17
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt
1 error in 0.24s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

import pytest
import yaml
import re
from unittest.mock import mock_open, patch

from your_module import initialise_prompt

@pytest.fixture
def agent():
    return "test_agent"

@pytest.fixture
def config_content():
    return """
    placeholder1: value1
    placeholder2: value2
    """

@pytest.fixture
def prompt_content():
    return "This is a {$placeholder1} and {$placeholder2} test."

@pytest.fixture
def expected_output():
    return "This is a value1 and value2 test."

def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("yaml.load", return_value=yaml.safe_load(config_content)):
            with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
                result = initialise_prompt(agent)
                assert result == expected_output
                mock_file.assert_called_once_with(config_path)
                mock_prompt_file.assert_called_once_with(prompt_path, "r")

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
temp\temp.py:22: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.37s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

import pytest
import yaml
import re
from unittest.mock import mock_open, patch

from your_module import initialise_prompt

@pytest.fixture
def agent():
    return "test_agent"

@pytest.fixture
def config_content():
    return """
    placeholder1: value1
    placeholder2: value2
    """

@pytest.fixture
def prompt_content():
    return "This is a {$placeholder1} and {$placeholder2} test."

@pytest.fixture
def expected_output():
    return "This is a value1 and value2 test."

def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("yaml.load", return_value=yaml.safe_load(config_content)):
            with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
                result = initialise_prompt(agent)
                assert result == expected_output
                mock_file.assert_called_once_with(config_path, "r")
                mock_prompt_file.assert_called_once_with(prompt_path, "r")

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
temp\temp.py:22: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s

TEST CASE 2 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

def test_initialise_prompt_missing_placeholder(agent, config_content, prompt_content):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
________ ERROR at setup of test_initialise_prompt_missing_placeholder _________
file C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py, line 17
  def test_initialise_prompt_missing_placeholder(agent, config_content, prompt_content):
E       fixture 'agent' not found
>       available fixtures: _session_event_loop, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, event_loop, event_loop_policy, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, mock_open_fixture, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, temp/temp.py::<event_loop>, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, unused_tcp_port, unused_tcp_port_factory, unused_udp_port, unused_udp_port_factory, yaml_load_fixture
>       use 'pytest --fixtures [testpath]' for help on them.

C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:17
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_missing_placeholder
1 error in 0.08s
TEST CASE 2 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

import os
import re
import yaml
import pytest


def initialise_prompt(agent: str):
    try:
        config_path = "./theory_evaluation/evaluator/prompts"
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        with open(f"{config_path}/{agent}/config.yaml") as file:
            config_values = yaml.load(file, Loader=yaml.loader.BaseLoader)

        with open(f"{config_path}/{agent}/prompt.txt", "r") as file:
            prompt_structure = file.read()

        pattern = r"\{\$(\w+)\}"
        for match in re.finditer(pattern, prompt_structure):
            placeholder = match.group(1)
            if placeholder in config_values:
                prompt_structure = re.sub(
                    r"\{\$" + placeholder + "\}",
                    config_values[placeholder],
                    prompt_structure,
                )
        return prompt_structure

    except Exception as e:
        print(f"{str(e)}: No configuration path to the prompt given.")


@pytest.fixture
def agent():
    return "test_agent"


@pytest.fixture
def config_content():
    return """
    placeholder1: value1
    placeholder2: value2
    """


@pytest.fixture
def prompt_content():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."


def test_initialise_prompt_missing_placeholder(agent, config_content, prompt_content, tmpdir):
    config_path = tmpdir.mkdir("theory_evaluation").mkdir("evaluator").mkdir("prompts").mkdir(agent)
    config_file = config_path.join("config.yaml")
    prompt_file = config_path.join("prompt.txt")

    config_file.write(config_content)
    prompt_file.write(prompt_content)

    result = initialise_prompt(agent)
    assert result == "This is a test prompt with value1 and value2."

---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_________________ test_initialise_prompt_missing_placeholder __________________
temp\temp.py:77: in test_initialise_prompt_missing_placeholder
    assert result == "This is a test prompt with value1 and value2."
E   AssertionError: assert None == 'This is a test prompt with value1 and value2.'
---------------------------- Captured stdout call -----------------------------
[Errno 2] No such file or directory: './theory_evaluation/evaluator/prompts/test_agent/config.yaml': No configuration path to the prompt given.
============================== warnings summary ===============================
temp\temp.py:40
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:40: SyntaxWarning: invalid escape sequence '\}'
    r"\{\$" + placeholder + "\}",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_missing_placeholder - AssertionEr...
1 failed, 1 warning in 0.34s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

import os
import re
import yaml
import pytest


def initialise_prompt(agent: str):
    try:
        config_path = "./theory_evaluation/evaluator/prompts"
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        with open(f"{config_path}/{agent}/config.yaml") as file:
            config_values = yaml.load(file, Loader=yaml.loader.BaseLoader)

        with open(f"{config_path}/{agent}/prompt.txt", "r") as file:
            prompt_structure = file.read()

        pattern = r"\{\$(\w+)\}"
        for match in re.finditer(pattern, prompt_structure):
            placeholder = match.group(1)
            if placeholder in config_values:
                prompt_structure = re.sub(
                    r"\{\$" + placeholder + "\}",
                    config_values[placeholder],
                    prompt_structure,
                )
        return prompt_structure

    except Exception as e:
        print(f"{str(e)}: No configuration path to the prompt given.")


@pytest.fixture
def agent():
    return "test_agent"


@pytest.fixture
def config_content():
    return """
    placeholder1: value1
    placeholder2: value2
    """


@pytest.fixture
def prompt_content():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."


def test_initialise_prompt_missing_placeholder(agent, config_content, prompt_content, tmpdir):
    config_path = tmpdir.mkdir("theory_evaluation").mkdir("evaluator").mkdir("prompts").mkdir(agent)
    config_file = config_path.join("config.yaml")
    prompt_file = config_path.join("prompt.txt")

    config_file.write(config_content)
    prompt_file.write(prompt_content)

    result = initialise_prompt(agent)
    assert result == "This is a test prompt with value1 and value2."

---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_________________ test_initialise_prompt_missing_placeholder __________________
temp\temp.py:77: in test_initialise_prompt_missing_placeholder
    assert result == "This is a test prompt with value1 and value2."
E   AssertionError: assert None == 'This is a test prompt with value1 and value2.'
---------------------------- Captured stdout call -----------------------------
[Errno 2] No such file or directory: './theory_evaluation/evaluator/prompts/test_agent/config.yaml': No configuration path to the prompt given.
============================== warnings summary ===============================
temp\temp.py:40
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:40: SyntaxWarning: invalid escape sequence '\}'
    r"\{\$" + placeholder + "\}",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_missing_placeholder - AssertionEr...
1 failed, 1 warning in 0.17s

TEST CASE 3 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____________________ test_initialise_prompt_file_not_found ____________________
temp\temp.py:19: in test_initialise_prompt_file_not_found
    with patch("builtins.open", side_effect=FileNotFoundError):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_file_not_found - NameError: name ...
1 failed in 0.21s
TEST CASE 3 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

from unittest.mock import patch
from your_module_name import initialise_prompt

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
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
temp\temp.py:18: in <module>
    from your_module_name import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.29s
TEST CASE 3 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

from unittest.mock import patch
from your_module_name import initialise_prompt

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
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
temp\temp.py:18: in <module>
    from your_module_name import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s

TEST CASE 5 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
___________________ test_initialise_settings_file_not_found ___________________
temp\temp.py:19: in test_initialise_settings_file_not_found
    with patch("builtins.open", side_effect=FileNotFoundError):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_file_not_found - NameError: nam...
1 failed in 0.19s
TEST CASE 5 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

from unittest.mock import patch
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 5 Retry 1 - Result - Failed
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
temp\temp.py:18: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.32s
TEST CASE 5 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def yaml_load_fixture():
    with patch("yaml.safe_load", return_value={}) as mocked_yaml_load:
        yield mocked_yaml_load

from unittest.mock import patch
from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_settings_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 5 Retry 2 - Result - Failed
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
temp\temp.py:18: in <module>
    from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.38s
