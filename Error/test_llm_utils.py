
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_prompt_returns_processed_prompt_on_valid_input(mock_open, mock_yaml_load, mock_re_finditer, mock_re_sub):
    # Arrange
    mock_open.return_value.read.return_value = "This is a {$placeholder} test."

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
1 error in 0.22s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

from unittest import mock
import pytest
import yaml

from temp.temp import initialise_prompt

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load", return_value={"placeholder": "replaced_value"}) as m:
        yield m

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as m:
        yield m

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", side_effect=lambda pattern, repl, string: string.replace("{$placeholder}", repl)) as m:
        yield m

def test_initialise_prompt_returns_processed_prompt_on_valid_input(mock_open, mock_yaml_load, mock_re_finditer, mock_re_sub):
    # Arrange
    mock_open.return_value.read.return_value = "This is a {$placeholder} test."

    # Act
    result = initialise_prompt("agent_name")

    # Assert
    assert result == "This is a replaced_value test."

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
1 error in 0.13s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

from unittest import mock
import pytest
import yaml

from temp.temp import initialise_prompt

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open()) as m:
        yield m

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.load", return_value={"placeholder": "replaced_value"}) as m:
        yield m

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as m:
        yield m

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", side_effect=lambda pattern, repl, string: string.replace("{$placeholder}", repl)) as m:
        yield m

def test_initialise_prompt_returns_processed_prompt_on_valid_input(mock_open, mock_yaml_load, mock_re_finditer, mock_re_sub):
    # Arrange
    mock_open.return_value.read.return_value = "This is a {$placeholder} test."

    # Act
    result = initialise_prompt("agent_name")

    # Assert
    assert result == "This is a replaced_value test."

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
1 error in 0.16s

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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_prompt_raises_exception_on_missing_config_path(mock_open):
    # Arrange
    with mock.patch("os.environ.get", return_value=None):
        # Act
        result = initialise_prompt("test_agent")

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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest import mock
from your_module import initialise_prompt

def test_initialise_prompt_raises_exception_on_missing_config_path():
    with mock.patch("os.environ.get", return_value=None):
        with mock.patch("builtins.open", mock.mock_open(read_data="")):
            with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                initialise_prompt("test_agent")

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
1 error in 0.18s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest import mock
from your_module import initialise_prompt

def test_initialise_prompt_raises_exception_on_missing_config_path():
    with mock.patch("os.environ.get", return_value=None):
        with mock.patch("builtins.open", mock.mock_open(read_data="")):
            with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                initialise_prompt("test_agent")

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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_settings_returns_settings_on_valid_input(mock_open, mock_yaml_safe_load):
    # Arrange
    mock_open.return_value.read.return_value = "setting: value"

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
1 error in 0.18s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_open():
    with patch("builtins.open", mock_open(read_data="setting: value")) as m:
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"setting": "value"}) as m:
        yield m

def test_initialise_settings_returns_settings_on_valid_input(mock_open, mock_yaml_safe_load):
    # Arrange
    agent = "refactor_code"
    
    # Act
    result = initialise_settings(agent)
    
    # Assert
    assert result == {"setting": "value"}

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
1 error in 0.19s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest.mock import patch, mock_open as mock_open_lib

@pytest.fixture
def mock_open():
    with patch("builtins.open", mock_open_lib(read_data="setting: value")) as m:
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"setting": "value"}) as m:
        yield m

def test_initialise_settings_returns_settings_on_valid_input(mock_open, mock_yaml_safe_load):
    # Arrange
    agent = "refactor_code"
    
    # Act
    result = initialise_settings(agent)
    
    # Assert
    assert result == {"setting": "value"}

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
1 error in 0.16s

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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

def test_initialise_settings_raises_exception_on_missing_config_path(mock_open):
    # Arrange
    with mock.patch("os.environ.get", return_value=None):
        # Act
        result = initialise_settings("test_agent")

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
1 error in 0.22s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest import mock
from your_module import initialise_settings

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open(read_data="data")) as m:
        yield m

def test_initialise_settings_raises_exception_on_missing_config_path(mock_open):
    with mock.patch("os.environ.get", return_value=None):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_settings("test_agent")

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
1 error in 0.24s
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
    with mock.patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with mock.patch("yaml.safe_load", return_value={"setting": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

@pytest.fixture
def mock_re_finditer():
    with mock.patch("re.finditer", return_value=[mock.Mock(group=lambda x: "placeholder")]) as mocked_re_finditer:
        yield mocked_re_finditer

@pytest.fixture
def mock_re_sub():
    with mock.patch("re.sub", return_value="processed prompt") as mocked_re_sub:
        yield mocked_re_sub

import pytest
from unittest import mock
from your_module import initialise_settings

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open(read_data="data")) as m:
        yield m

@pytest.fixture
def mock_yaml_load():
    with mock.patch("yaml.safe_load", return_value={"key": "value"}) as m:
        yield m

def test_initialise_settings_raises_exception_on_missing_config_path(mock_open, mock_yaml_load):
    with mock.patch("os.environ.get", return_value=None):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_settings("test_agent")

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
