
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_prompt_success(mock_config_path, mock_yaml_load, mock_prompt_structure):
    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_yaml_load))) as mock_file:
        with patch('yaml.load', return_value=mock_yaml_load):
            with patch('re.finditer', return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure)):
                with patch('re.sub', side_effect=lambda pattern, repl, string: string.replace("{$placeholder1}", "value1").replace("{$placeholder2}", "value2")):
                    result = initialise_prompt('agent_name')
                    assert result == "This is a test prompt with value1 and value2."
                    mock_file.assert_any_call(f"{mock_config_path}/agent_name/config.yaml")
                    mock_file.assert_any_call(f"{mock_config_path}/agent_name/prompt.txt", "r")

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:30: in test_initialise_prompt_success
    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_yaml_load))) as mock_file:
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - NameError: name 'patch'...
1 failed in 0.23s
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
import yaml
import re
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_yaml_load = {'placeholder1': 'value1', 'placeholder2': 'value2'}
    mock_prompt_structure = "This is a test prompt with {$placeholder1} and {$placeholder2}."

    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_yaml_load))) as mock_file:
        with patch('yaml.load', return_value=mock_yaml_load):
            with patch('re.finditer', return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure)):
                with patch('re.sub', side_effect=lambda pattern, repl, string: string.replace("{$placeholder1}", "value1").replace("{$placeholder2}", "value2")):
                    result = initialise_prompt('agent_name')
                    assert result == "This is a test prompt with value1 and value2."
                    mock_file.assert_any_call(f"{mock_config_path}/agent_name/config.yaml")
                    mock_file.assert_any_call(f"{mock_config_path}/agent_name/prompt.txt", "r")

---------------
TEST CASE 1 Retry 1 - Result - Failed
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
temp\temp.py:32: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
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

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
import yaml
import re
from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_prompt_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_yaml_load = {'placeholder1': 'value1', 'placeholder2': 'value2'}
    mock_prompt_structure = "This is a test prompt with {$placeholder1} and {$placeholder2}."

    with patch('builtins.open', mock_open(read_data="placeholder1: value1\nplaceholder2: value2")) as mock_file:
        with patch('yaml.load', return_value=mock_yaml_load):
            with patch('re.finditer', return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure)):
                with patch('re.sub', side_effect=lambda pattern, repl, string: string.replace("{$placeholder1}", "value1").replace("{$placeholder2}", "value2")):
                    result = initialise_prompt('agent_name')
                    assert result == "This is a test prompt with value1 and value2."
                    mock_file.assert_any_call(f"{mock_config_path}/agent_name/config.yaml")
                    mock_file.assert_any_call(f"{mock_config_path}/agent_name/prompt.txt", "r")

---------------
TEST CASE 1 Retry 2 - Result - Failed
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
temp\temp.py:32: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s

TEST CASE 2 Retry 0
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_prompt_no_config_path():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('yaml.load', return_value={}):
            with patch('re.finditer', return_value=[]):
                result = initialise_prompt('agent_name')
                assert result is None

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____________________ test_initialise_prompt_no_config_path ____________________
temp\temp.py:30: in test_initialise_prompt_no_config_path
    with patch('builtins.open', mock_open()) as mock_file:
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_no_config_path - NameError: name ...
1 failed in 0.23s
TEST CASE 2 Retry 1
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt_no_config_path():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('yaml.load', return_value={}):
            with patch('re.finditer', return_value=[]):
                result = initialise_prompt('agent_name')
                assert result is None

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
temp\temp.py:30: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.31s
TEST CASE 2 Retry 2
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_prompt_no_config_path():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('yaml.load', return_value={}):
            with patch('re.finditer', return_value=[]):
                result = initialise_prompt('agent_name')
                assert result is None

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
temp\temp.py:30: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.31s

TEST CASE 3 Retry 0
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_settings_success(mock_config_path, mock_llm_settings):
    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_llm_settings))) as mock_file:
        with patch('yaml.safe_load', return_value=mock_llm_settings):
            result = initialise_settings('agent_name')
            assert result == mock_llm_settings
            mock_file.assert_called_once_with(f"{mock_config_path}/agent_name/llm_settings.yaml")

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
______________________ test_initialise_settings_success _______________________
temp\temp.py:30: in test_initialise_settings_success
    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_llm_settings))) as mock_file:
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_success - NameError: name 'patc...
1 failed in 0.12s
TEST CASE 3 Retry 1
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
import yaml
import pytest
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings = {'key': 'value'}  # Replace with actual mock data structure

    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_llm_settings))) as mock_file:
        with patch('yaml.safe_load', return_value=mock_llm_settings):
            result = initialise_settings('agent_name')
            assert result == mock_llm_settings
            mock_file.assert_called_once_with(f"{mock_config_path}/agent_name/llm_settings.yaml")

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
temp\temp.py:32: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
TEST CASE 3 Retry 2
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
import yaml
import pytest
from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_settings_success():
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_llm_settings = {'key': 'value'}  # Replace with actual mock data structure

    with patch('builtins.open', mock_open(read_data=yaml.dump(mock_llm_settings))) as mock_file:
        with patch('yaml.safe_load', return_value=mock_llm_settings):
            result = initialise_settings('agent_name')
            assert result == mock_llm_settings
            mock_file.assert_called_once_with(f"{mock_config_path}/agent_name/llm_settings.yaml")

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
temp\temp.py:32: in <module>
    from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.33s

TEST CASE 4 Retry 0
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

def test_initialise_settings_no_config_path():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('yaml.safe_load', return_value={}):
            result = initialise_settings('agent_name')
            assert result is None

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
___________________ test_initialise_settings_no_config_path ___________________
temp\temp.py:30: in test_initialise_settings_no_config_path
    with patch('builtins.open', mock_open()) as mock_file:
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_no_config_path - NameError: nam...
1 failed in 0.20s
TEST CASE 4 Retry 1
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
import yaml
from your_module import initialise_settings  # replace 'your_module' with the actual module name

def test_initialise_settings_no_config_path():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('yaml.safe_load', return_value={}):
            result = initialise_settings('agent_name')
            assert result is None

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
temp\temp.py:31: in <module>
    from your_module import initialise_settings  # replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.34s
TEST CASE 4 Retry 2
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
def mock_yaml_load():
    return {
        'placeholder1': 'value1',
        'placeholder2': 'value2'
    }

@pytest.fixture
def mock_prompt_structure():
    return "This is a test prompt with {$placeholder1} and {$placeholder2}."

@pytest.fixture
def mock_llm_settings():
    return {
        'setting1': 'value1',
        'setting2': 'value2'
    }

from unittest.mock import patch, mock_open
import yaml
from your_actual_module_name import initialise_settings  # replace 'your_actual_module_name' with the actual module name

def test_initialise_settings_no_config_path():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('yaml.safe_load', return_value=None):
            result = initialise_settings('agent_name')
            assert result is None

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
temp\temp.py:31: in <module>
    from your_actual_module_name import initialise_settings  # replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.36s
