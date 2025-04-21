
TEST CASE 1 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

def test_initialise_prompt_success(mock_agent, mock_open_files, mock_yaml_load, mock_config_path):
    expected_output = "Hello, World!"
    result = initialise_prompt(mock_agent)
    assert result == expected_output
    mock_open_files.assert_any_call(f"{mock_config_path}/{mock_agent}/config.yaml")
    mock_open_files.assert_any_call(f"{mock_config_path}/{mock_agent}/prompt.txt")
    mock_yaml_load.assert_called_once()

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
______________ ERROR at setup of test_initialise_prompt_success _______________
temp\temp.py:35: in mock_open_files
    m = mock_open(read_data=mock_prompt_structure)
E   NameError: name 'mock_open' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_prompt_success - NameError: name 'mock_op...
1 error in 0.45s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

from unittest.mock import patch, mock_open
import pytest
import yaml

from your_module import initialise_prompt  # Replace with the actual module name

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_path, mock_agent):
    m = mock_open(read_data=mock_prompt_structure)
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch("yaml.load", return_value=mock_config_values) as mock_load:
        yield mock_load

def test_initialise_prompt_success(mock_agent, mock_open_files, mock_yaml_load, mock_config_path):
    expected_output = "Hello, World!"
    result = initialise_prompt(mock_agent)
    assert result == expected_output
    mock_open_files.assert_any_call(f"{mock_config_path}/{mock_agent}/config.yaml")
    mock_open_files.assert_any_call(f"{mock_config_path}/{mock_agent}/prompt.txt")
    mock_yaml_load.assert_called_once()

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
temp\temp.py:43: in <module>
    from your_module import initialise_prompt  # Replace with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

from unittest.mock import patch, mock_open
import pytest
import yaml

from your_actual_module_name import initialise_prompt  # Replace with the actual module name

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_path, mock_agent):
    m = mock_open(read_data=mock_prompt_structure)
    with patch("builtins.open", m):
        yield m

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch("yaml.load", return_value=mock_config_values) as mock_load:
        yield mock_load

def test_initialise_prompt_success(mock_agent, mock_open_files, mock_yaml_load, mock_config_path):
    expected_output = "Hello, World!"
    result = initialise_prompt(mock_agent)
    assert result == expected_output
    mock_open_files.assert_any_call(f"{mock_config_path}/{mock_agent}/config.yaml")
    mock_open_files.assert_any_call(f"{mock_config_path}/{mock_agent}/prompt.txt")
    mock_yaml_load.assert_called_once()

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
temp\temp.py:43: in <module>
    from your_actual_module_name import initialise_prompt  # Replace with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
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
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

def test_initialise_settings_file_not_found(mock_agent, mock_open_files):
    mock_open_files.side_effect = FileNotFoundError
    result = initialise_settings(mock_agent)
    assert result is None

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________ ERROR at setup of test_initialise_settings_file_not_found __________
temp\temp.py:35: in mock_open_files
    m = mock_open(read_data=mock_prompt_structure)
E   NameError: name 'mock_open' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py::test_initialise_settings_file_not_found - NameError: name...
1 error in 0.16s
TEST CASE 5 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

import pytest
from unittest.mock import patch, mock_open
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
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
temp\temp.py:41: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.30s
TEST CASE 5 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_agent():
    return "test_agent"

@pytest.fixture
def mock_prompt_structure():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_values():
    return {"name": "World"}

@pytest.fixture
def mock_yaml_load(mock_config_values):
    with patch('yaml.load', return_value=mock_config_values) as mock_load:
        yield mock_load

@pytest.fixture
def mock_yaml_safe_load(mock_config_values):
    with patch('yaml.safe_load', return_value=mock_config_values) as mock_safe_load:
        yield mock_safe_load

@pytest.fixture
def mock_open_files(mock_prompt_structure, mock_config_values):
    m = mock_open(read_data=mock_prompt_structure)
    with patch('builtins.open', m):
        yield m

import pytest
from unittest.mock import patch, mock_open
from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_settings_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings("non_existent_agent")
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
temp\temp.py:41: in <module>
    from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s
