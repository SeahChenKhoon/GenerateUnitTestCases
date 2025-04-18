
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_prompt_returns_expected_output_on_valid_input(mock_open, mock_yaml_load, mock_re_finditer, mock_re_sub):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "Prompt with {$key} placeholder"
    result = initialise_prompt(agent)
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt", "r")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()
    assert result == "modified_prompt_structure"

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load") as mock:
        yield mock

@pytest.fixture
def mock_re_finditer():
    with patch("re.finditer") as mock:
        yield mock

@pytest.fixture
def mock_re_sub():
    with patch("re.sub") as mock:
        yield mock

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data="Prompt with {$key} placeholder")) as mock:
        yield mock

def test_initialise_prompt_returns_expected_output_on_valid_input(mock_open_file, mock_yaml_load, mock_re_finditer, mock_re_sub):
    agent = "test_agent"
    mock_yaml_load.return_value = {"key": "value"}
    mock_re_finditer.return_value = [re.Match]
    mock_re_sub.return_value = "modified_prompt_structure"
    
    result = initialise_prompt(agent)
    
    mock_open_file.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open_file.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt", "r")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()
    assert result == "modified_prompt_structure"

---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.16s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open
import re

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load") as mock:
        yield mock

@pytest.fixture
def mock_re_finditer():
    with patch("re.finditer") as mock:
        yield mock

@pytest.fixture
def mock_re_sub():
    with patch("re.sub") as mock:
        yield mock

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data="Prompt with {$key} placeholder")) as mock:
        yield mock

def test_initialise_prompt_returns_expected_output_on_valid_input(mock_open_file, mock_yaml_load, mock_re_finditer, mock_re_sub):
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

    agent = "test_agent"
    mock_yaml_load.return_value = {"key": "value"}
    mock_re_finditer.return_value = [re.Match]
    mock_re_sub.return_value = "modified_prompt_structure"
    
    result = initialise_prompt(agent)
    
    mock_open_file.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/config.yaml")
    mock_open_file.assert_any_call("./theory_evaluation/evaluator/prompts/test_agent/prompt.txt", "r")
    mock_yaml_load.assert_called_once()
    mock_re_finditer.assert_called_once()
    mock_re_sub.assert_called_once()
    assert result == "modified_prompt_structure"

---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.15s

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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_prompt_handles_missing_config_file(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_prompt(agent)
    assert result is None

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_open():
    with patch("builtins.open", mock_open()) as m:
        yield m

def test_initialise_prompt_handles_missing_config_file(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_prompt(agent)
    assert result is None

---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.17s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as m:
        yield m

def test_initialise_prompt_handles_missing_config_file(mock_open_fixture):
    agent = "test_agent"
    mock_open_fixture.side_effect = FileNotFoundError
    result = initialise_prompt(agent)
    assert result is None

---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.13s

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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_prompt_handles_missing_placeholder(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "Prompt with {$missing_key} placeholder"
    mock_yaml_load.return_value = {"key": "value"}
    result = initialise_prompt(agent)
    assert result == "Prompt with {$missing_key} placeholder"

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch

@pytest.fixture
def mock_open(mocker):
    return mocker.patch("builtins.open", mocker.mock_open())

@pytest.fixture
def mock_yaml_load(mocker):
    return mocker.patch("yaml.load")

@pytest.fixture
def mock_re_finditer(mocker):
    return mocker.patch("re.finditer")

def test_initialise_prompt_handles_missing_placeholder(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "Prompt with {$missing_key} placeholder"
    mock_yaml_load.return_value = {"key": "value"}
    mock_re_finditer.return_value = iter([])  # No matches for the placeholder pattern
    result = initialise_prompt(agent)
    assert result == "Prompt with {$missing_key} placeholder"

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch

@pytest.fixture
def mock_open(mocker):
    return mocker.patch("builtins.open", mocker.mock_open())

@pytest.fixture
def mock_yaml_load(mocker):
    return mocker.patch("yaml.load")

@pytest.fixture
def mock_re_finditer(mocker):
    return mocker.patch("re.finditer")

def test_initialise_prompt_handles_missing_placeholder(mock_open, mock_yaml_load, mock_re_finditer):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "Prompt with {$missing_key} placeholder"
    mock_yaml_load.return_value = {"key": "value"}
    mock_re_finditer.return_value = iter([])  # No matches for the placeholder pattern
    result = initialise_prompt(agent)
    assert result == "Prompt with {$missing_key} placeholder"

---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.12s

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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_settings_returns_expected_output_on_valid_input(mock_open, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()
    assert result == {"setting": "value"}

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.21s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open
import yaml
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_open():
    with patch("builtins.open", mock_open(read_data="data")) as mock_file:
        yield mock_file

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"setting": "value"}) as mock_yaml:
        yield mock_yaml

def test_initialise_settings_returns_expected_output_on_valid_input(mock_open, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()
    assert result == {"setting": "value"}

---------------
TEST CASE 4 Retry 1 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open as mock_open_lib
import yaml
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_open():
    with patch("builtins.open", mock_open_lib(read_data="data")) as mock_file:
        yield mock_file

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"setting": "value"}) as mock_yaml:
        yield mock_yaml

def test_initialise_settings_returns_expected_output_on_valid_input(mock_open, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    mock_open.assert_called_once_with("./theory_evaluation/evaluator/prompts/test_agent/llm_settings.yaml")
    mock_yaml_safe_load.assert_called_once()
    assert result == {"setting": "value"}

---------------
TEST CASE 4 Retry 2 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.22s

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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_settings_handles_missing_config_file(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_open():
    with patch("builtins.open", mock_open()) as m:
        yield m

def test_initialise_settings_handles_missing_config_file(mock_open):
    agent = "test_agent"
    mock_open.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 1 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.20s
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_open_fixture():
    with patch("builtins.open", mock_open()) as m:
        yield m

def test_initialise_settings_handles_missing_config_file(mock_open_fixture):
    agent = "test_agent"
    mock_open_fixture.side_effect = FileNotFoundError
    result = initialise_settings(agent)
    assert result is None

---------------
TEST CASE 5 Retry 2 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s

TEST CASE 6 Retry 0
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_settings_handles_invalid_yaml(mock_open):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "invalid_yaml"
    with mock.patch("yaml.safe_load", side_effect=yaml.YAMLError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 6 Retry 0 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.22s
TEST CASE 6 Retry 1
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

from unittest import mock
import yaml

def test_initialise_settings_handles_invalid_yaml(mock_open):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "invalid_yaml"
    with mock.patch("yaml.safe_load", side_effect=yaml.YAMLError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 6 Retry 1 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.22s
TEST CASE 6 Retry 2
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
    with mock.patch("yaml.load", return_value={"key": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=iter([mock.Mock(group=lambda x: "key")])) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="modified_prompt_structure") as mocked_re_sub:
        yield mocked_re_sub

from unittest import mock
import pytest
import yaml

@pytest.fixture
def mock_open(mocker):
    return mocker.patch("builtins.open", mock.mock_open())

def test_initialise_settings_handles_invalid_yaml(mock_open):
    agent = "test_agent"
    mock_open.return_value.read.return_value = "invalid_yaml"
    with mock.patch("yaml.safe_load", side_effect=yaml.YAMLError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 6 Retry 2 - Result - Failed
Test Error - C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:3: in <module>
    import yaml
E   ModuleNotFoundError: No module named 'yaml'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
