
TEST CASE 4 Retry 0
---------------
import yaml
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_settings_normal_behavior(mock_open_yaml, mock_yaml_safe_load, mock_config_path):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {"setting": "value"}
---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:5: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.31s
TEST CASE 4 Retry 1
---------------
import os
from theory_evaluation.llm_utils import initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_settings_normal_behavior(mock_open_yaml, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {"setting": "value"}
---------------
TEST CASE 4 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________ ERROR at setup of test_initialise_settings_normal_behavior __________
temp\temp.py:19: in mock_yaml_safe_load
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1479: in __enter__
    self.target = self.getter()
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\pkgutil.py:513: in resolve_name
    mod = importlib.import_module(modname)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1324: in _find_and_load_unlocked
    ???
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_normal_behavior - ModuleNotFound...
1 error in 0.23s
TEST CASE 4 Retry 2
---------------
import os
from theory_evaluation.llm_utils import initialise_settings
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_open_prompt():
    m = mock_open(read_data="Hello, {$key}!")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load", return_value={"key": "value"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_settings_normal_behavior(mock_open_yaml, mock_yaml_safe_load):
    agent = "test_agent"
    result = initialise_settings(agent)
    assert result == {"setting": "value"}
---------------
TEST CASE 4 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________ ERROR at setup of test_initialise_settings_normal_behavior __________
temp\temp.py:30: in mock_yaml_safe_load
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1479: in __enter__
    self.target = self.getter()
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\pkgutil.py:513: in resolve_name
    mod = importlib.import_module(modname)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1324: in _find_and_load_unlocked
    ???
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_normal_behavior - ModuleNotFound...
1 error in 0.30s

TEST CASE 5 Retry 0
---------------
import os
from theory_evaluation.llm_utils import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

def test_initialise_settings_file_not_found(mock_config_path):
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

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:4: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.30s
TEST CASE 5 Retry 1
---------------
import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_open_prompt():
    m = mock_open(read_data="Hello, {$key}!")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load", return_value={"key": "value"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

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
temp\temp.py:3: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.21s
TEST CASE 5 Retry 2
---------------
import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_open_prompt():
    m = mock_open(read_data="Hello, {$key}!")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load", return_value={"key": "value"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

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
temp\temp.py:3: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.17s

TEST CASE 6 Retry 0
---------------
import yaml
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_settings_invalid_yaml(mock_open_yaml, mock_config_path):
    agent = "test_agent"
    with patch("your_module.yaml.safe_load", side_effect=yaml.YAMLError):
        result = initialise_settings(agent)
    assert result is None
---------------
TEST CASE 6 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:5: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s
TEST CASE 6 Retry 1
---------------
import os
import yaml
import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_open_prompt():
    m = mock_open(read_data="Hello, {$key}!")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load", return_value={"key": "value"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_settings_invalid_yaml():
    agent = "test_agent"
    with patch("your_module.yaml.safe_load", side_effect=yaml.YAMLError):
        result = initialise_settings(agent)
    assert result is None
---------------
TEST CASE 6 Retry 1 - Result - Failed
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
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s
TEST CASE 6 Retry 2
---------------
import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt
import pytest
from unittest.mock import patch, mock_open
from yaml import YAMLError
from your_module import initialise_settings

@pytest.fixture
def mock_config_path():
    with patch("your_module.os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_open_yaml():
    m = mock_open(read_data="key: value")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_open_prompt():
    m = mock_open(read_data="Hello, {$key}!")
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load():
    with patch("your_module.yaml.load", return_value={"key": "value"}):
        yield

@pytest.fixture
def mock_yaml_safe_load():
    with patch("your_module.yaml.safe_load", return_value={"setting": "value"}):
        yield

def test_initialise_settings_invalid_yaml():
    agent = "test_agent"
    with patch("yaml.safe_load", side_effect=YAMLError):
        result = initialise_settings(agent)
    assert result is None
---------------
TEST CASE 6 Retry 2 - Result - Failed
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
temp\temp.py:7: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.25s
