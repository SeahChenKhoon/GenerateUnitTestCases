
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
        mock.mock_open(read_data="{'key': 'value'}").return_value,
        mock.mock_open(read_data="Hello, {$key}!").return_value
    ]
    mock_yaml_load.return_value = {'key': 'value'}
    mock_re_finditer.return_value = [mock.Mock(group=lambda: 'key')]
    mock_re_sub.return_value = "Hello, value!"
    result = initialise_prompt(agent)
    assert result == "Hello, value!"
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
1 error in 0.21s
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

from unittest import mock
import pytest
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

@mock.patch("builtins.open", new_callable=mock.mock_open)
@mock.patch("yaml.load")
@mock.patch("re.finditer")
@mock.patch("re.sub")
def test_initialise_prompt_success(mock_re_sub, mock_re_finditer, mock_yaml_load, mock_open):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="{'key': 'value'}").return_value,
        mock.mock_open(read_data="Hello, {$key}!").return_value
    ]
    mock_yaml_load.return_value = {'key': 'value'}
    mock_re_finditer.return_value = [mock.Mock(group=lambda: 'key')]
    mock_re_sub.return_value = "Hello, value!"
    result = initialise_prompt(agent)
    assert result == "Hello, value!"
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()

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
temp\temp.py:34: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.25s
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

from unittest import mock
import pytest
from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name

@mock.patch("builtins.open", new_callable=mock.mock_open)
@mock.patch("yaml.load")
@mock.patch("re.finditer")
@mock.patch("re.sub")
def test_initialise_prompt_success(mock_re_sub, mock_re_finditer, mock_yaml_load, mock_open):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="key: value").return_value,
        mock.mock_open(read_data="Hello, {$key}!").return_value
    ]
    mock_yaml_load.return_value = {'key': 'value'}
    mock_re_finditer.return_value = [mock.Mock(group=lambda x=1: 'key')]
    mock_re_sub.return_value = "Hello, value!"
    result = initialise_prompt(agent)
    assert result == "Hello, value!"
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()

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
temp\temp.py:34: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.29s

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

def test_initialise_prompt_no_config_path(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_prompt(agent)
    assert result is None

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
___________ ERROR at setup of test_initialise_prompt_no_config_path ___________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_no_config_path - NameError: name '...
1 error in 0.19s
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

from unittest import mock
import pytest
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        result = initialise_prompt(agent)
        assert result is None

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
temp\temp.py:34: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.35s
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

from unittest import mock
import pytest
from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_prompt_no_config_path():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        result = initialise_prompt(agent)
        assert result is None

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
temp\temp.py:34: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
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

def test_initialise_prompt_placeholder_not_in_config(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.side_effect = [
        mock.mock_open(read_data="{'another_key': 'value'}").return_value,
        mock.mock_open(read_data="Hello, {$key}!").return_value
    ]
    mock_yaml_load.return_value = {'another_key': 'value'}
    mock_re_finditer.return_value = [mock.Mock(group=lambda: 'key')]
    result = initialise_prompt(agent)
    assert result == "Hello, {$key}!"

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_____ ERROR at setup of test_initialise_prompt_placeholder_not_in_config ______
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_placeholder_not_in_config - NameEr...
1 error in 0.17s
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

from unittest import mock
from your_module import initialise_prompt

def test_initialise_prompt_placeholder_not_in_config():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open(read_data="{'another_key': 'value'}")) as mock_open:
        with mock.patch("yaml.load", return_value={'another_key': 'value'}) as mock_yaml_load:
            with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda: 'key')]) as mock_re_finditer:
                result = initialise_prompt(agent)
                assert result == "Hello, {$key}!"

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
temp\temp.py:33: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.30s
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

from unittest import mock
from your_module import initialise_prompt

def test_initialise_prompt_placeholder_not_in_config():
    agent = "test_agent"
    mock_prompt = "Hello, {$key}!"
    mock_config = {'another_key': 'value'}
    
    with mock.patch("builtins.open", mock.mock_open(read_data=mock_prompt)) as mock_open:
        with mock.patch("yaml.load", return_value=mock_config) as mock_yaml_load:
            with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x=1: 'key')]) as mock_re_finditer:
                result = initialise_prompt(agent)
                assert result == "Hello, {$key}!"

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
temp\temp.py:33: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s

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
    mock_open.return_value = mock.mock_open(read_data="{'setting_key': 'setting_value'}").return_value
    mock_yaml_safe_load.return_value = {'setting_key': 'setting_value'}
    result = initialise_settings(agent)
    assert result == {'setting_key': 'setting_value'}
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
1 error in 0.23s
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

from unittest import mock
import pytest
import yaml
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="setting_key: setting_value")
@mock.patch("yaml.safe_load", return_value={'setting_key': 'setting_value'})
def test_initialise_settings_success(mock_yaml_safe_load, mock_open):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {'setting_key': 'setting_value'}
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

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
temp\temp.py:35: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.28s
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

from unittest import mock
import pytest
import yaml
from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name

@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="setting_key: setting_value")
@mock.patch("yaml.safe_load", return_value={'setting_key': 'setting_value'})
def test_initialise_settings_success(mock_yaml_safe_load, mock_open):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {'setting_key': 'setting_value'}
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()

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
temp\temp.py:35: in <module>
    from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.19s

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

def test_initialise_settings_no_config_path(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________ ERROR at setup of test_initialise_settings_no_config_path __________
temp\temp.py:9: in mock_open
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
E   NameError: name 'mock' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_no_config_path - NameError: name...
1 error in 0.32s
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

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
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
temp\temp.py:34: in <module>
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
from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_settings_no_config_path():
    agent = "test_agent"
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError
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
temp\temp.py:34: in <module>
    from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.29s
