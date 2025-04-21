
TEST CASE 1 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

def test_initialise_prompt_success(mock_open, mock_yaml_load, mock_re_finditer, mock_re_sub):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="prompt text with {$placeholder}").return_value,
        mock.mock_open(read_data="config_value").return_value
    ]
    mock_yaml_load.return_value = {"placeholder": "replaced_value"}
    mock_re_finditer.return_value = [mock.Mock(group=lambda: "placeholder")]
    mock_re_sub.return_value = "prompt text with replaced_value"
    result = initialise_prompt(agent)
    assert result == "prompt text with replaced_value"
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
______________ ERROR at setup of test_initialise_prompt_success _______________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_success - NameError: name 'mock' i...
1 error in 0.30s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import os
import re
import yaml
from unittest import mock

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_open = mock.mock_open()
    mock_open.side_effect = [
        mock.mock_open(read_data="prompt text with {$placeholder}").return_value,
        mock.mock_open(read_data="config_value").return_value
    ]
    with mock.patch("builtins.open", mock_open):
        with mock.patch("yaml.load", return_value={"placeholder": "replaced_value"}) as mock_yaml_load:
            with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda: "placeholder")]) as mock_re_finditer:
                with mock.patch("re.sub", return_value="prompt text with replaced_value") as mock_re_sub:
                    result = initialise_prompt(agent)
                    assert result == "prompt text with replaced_value"
                    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
                    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt")
                    mock_yaml_load.assert_called_once()
                    mock_re_finditer.assert_called_once()
                    mock_re_sub.assert_called_once()

---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:49: in test_initialise_prompt_success
    assert result == "prompt text with replaced_value"
E   AssertionError: assert None == 'prompt text with replaced_value'
---------------------------- Captured stdout call -----------------------------
test_initialise_prompt_success.<locals>.<lambda>() takes 0 positional arguments but 1 was given: No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - AssertionError: assert ...
1 failed in 0.20s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import os
import re
import yaml
from unittest import mock
from unittest import TestCase

class TestInitialisePrompt(TestCase):
    def test_initialise_prompt_success(self):
        agent = "test_agent"
        mock_open = mock.mock_open()
        mock_open.side_effect = [
            mock.mock_open(read_data="config_value: replaced_value").return_value,
            mock.mock_open(read_data="prompt text with {$placeholder}").return_value
        ]
        with mock.patch("builtins.open", mock_open):
            with mock.patch("yaml.load", return_value={"placeholder": "replaced_value"}) as mock_yaml_load:
                with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda: "placeholder")]) as mock_re_finditer:
                    with mock.patch("re.sub", return_value="prompt text with replaced_value") as mock_re_sub:
                        result = initialise_prompt(agent)
                        assert result == "prompt text with replaced_value"
                        mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
                        mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt")
                        mock_yaml_load.assert_called_once()
                        mock_re_finditer.assert_called_once()
                        mock_re_sub.assert_called_once()

---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_____________ TestInitialisePrompt.test_initialise_prompt_success _____________
temp\temp.py:51: in test_initialise_prompt_success
    assert result == "prompt text with replaced_value"
E   AssertionError: assert None == 'prompt text with replaced_value'
---------------------------- Captured stdout call -----------------------------
TestInitialisePrompt.test_initialise_prompt_success.<locals>.<lambda>() takes 0 positional arguments but 1 was given: No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::TestInitialisePrompt::test_initialise_prompt_success - A...
1 failed in 0.22s

TEST CASE 2 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

def test_initialise_prompt_missing_placeholder(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="prompt text with {$missing_placeholder}").return_value,
        mock.mock_open(read_data="config_value").return_value
    ]
    mock_yaml_load.return_value = {"placeholder": "replaced_value"}
    mock_re_finditer.return_value = [mock.Mock(group=lambda: "missing_placeholder")]
    result = initialise_prompt(agent)
    assert result == "prompt text with {$missing_placeholder}"

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
________ ERROR at setup of test_initialise_prompt_missing_placeholder _________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_missing_placeholder - NameError: n...
1 error in 0.15s
TEST CASE 2 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from your_module import initialise_prompt

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_re_finditer:
        yield mocked_re_finditer

def test_initialise_prompt_missing_placeholder(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="prompt text with {$missing_placeholder}").return_value,
        mock.mock_open(read_data="config_value").return_value
    ]
    mock_yaml_load.return_value = {"placeholder": "replaced_value"}
    mock_re_finditer.return_value = [mock.Mock(group=lambda x=1: "missing_placeholder")]
    result = initialise_prompt(agent)
    assert result == "prompt text with {$missing_placeholder}"

---------------
TEST CASE 2 Retry 1 - Result - Failed
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
temp\temp.py:34: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.41s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from source_code_module import initialise_prompt

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_re_finditer:
        yield mocked_re_finditer

def test_initialise_prompt_missing_placeholder(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="prompt text with {$missing_placeholder}").return_value,
        mock.mock_open(read_data="config_value").return_value
    ]
    mock_yaml_load.return_value = {"missing_placeholder": "replaced_value"}
    mock_re_finditer.return_value = [mock.Mock(group=lambda x=1: "missing_placeholder")]
    result = initialise_prompt(agent)
    assert result == "prompt text with replaced_value"

---------------
TEST CASE 2 Retry 2 - Result - Failed
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
temp\temp.py:34: in <module>
    from source_code_module import initialise_prompt
E   ModuleNotFoundError: No module named 'source_code_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.25s

TEST CASE 3 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

def test_initialise_prompt_file_not_found(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_prompt(agent)
    assert result is None

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
___________ ERROR at setup of test_initialise_prompt_file_not_found ___________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_file_not_found - NameError: name '...
1 error in 0.16s
TEST CASE 3 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from source_code import initialise_prompt

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        result = initialise_prompt(agent)
        assert result is None

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
temp\temp.py:34: in <module>
    from source_code import initialise_prompt
E   ModuleNotFoundError: No module named 'source_code'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s
TEST CASE 3 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from your_module_name import initialise_prompt  # Replace 'your_module_name' with the actual module name

def test_initialise_prompt_file_not_found():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        result = initialise_prompt(agent)
        assert result is None

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
temp\temp.py:34: in <module>
    from your_module_name import initialise_prompt  # Replace 'your_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.29s

TEST CASE 4 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

def test_initialise_settings_success(mock_open, mock_yaml_safe_load):
    agent = "test_agent"
    mock_open.return_value = mock.mock_open(read_data="llm_settings_data").return_value
    mock_yaml_safe_load.return_value = {"setting_key": "setting_value"}
    result = initialise_settings(agent)
    assert result == {"setting_key": "setting_value"}
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_____________ ERROR at setup of test_initialise_settings_success ______________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_success - NameError: name 'mock'...
1 error in 0.13s
TEST CASE 4 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from your_module import initialise_settings

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open(read_data="llm_settings_data")) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting_key": "setting_value"}) as mocked_yaml:
        yield mocked_yaml

def test_initialise_settings_success(mock_open, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {"setting_key": "setting_value"}
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

---------------
TEST CASE 4 Retry 1 - Result - Failed
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
temp\temp.py:34: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.39s
TEST CASE 4 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from your_actual_module_name import initialise_settings

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open(read_data="llm_settings_data")) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting_key": "setting_value"}) as mocked_yaml:
        yield mocked_yaml

def test_initialise_settings_success(mock_open, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {"setting_key": "setting_value"}
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

---------------
TEST CASE 4 Retry 2 - Result - Failed
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
temp\temp.py:34: in <module>
    from your_actual_module_name import initialise_settings
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.39s

TEST CASE 5 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

def test_initialise_settings_file_not_found(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________ ERROR at setup of test_initialise_settings_file_not_found __________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_file_not_found - NameError: name...
1 error in 0.23s
TEST CASE 5 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_initialise_settings_file_not_found(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 1 - Result - Failed
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
temp\temp.py:34: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.29s
TEST CASE 5 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load") as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load") as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer") as mocked_finditer:
        yield mocked_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub") as mocked_sub:
        yield mocked_sub

import pytest
from unittest import mock
from my_module import initialise_settings  # Replace 'my_module' with the actual module name

@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_initialise_settings_file_not_found(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 2 - Result - Failed
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
temp\temp.py:34: in <module>
    from my_module import initialise_settings  # Replace 'my_module' with the actual module name
E   ModuleNotFoundError: No module named 'my_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
