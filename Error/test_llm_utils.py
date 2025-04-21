
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
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_yaml_load))) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_load):
            with patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure)):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace("{$placeholder1}", "value1").replace("{$placeholder2}", "value2")):
                    result = initialise_prompt(agent)
                    assert result == "This is a test prompt with value1 and value2."
                    mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
                    mock_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:31: in test_initialise_prompt_success
    with patch("builtins.open", mock_open(read_data=yaml.dump(mock_yaml_load))) as mock_file:
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
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_yaml_load = {"placeholder1": "value1", "placeholder2": "value2"}
    mock_prompt_structure = "This is a test prompt with {$placeholder1} and {$placeholder2}."

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_load):
            with patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_structure)):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace("{$placeholder1}", "value1").replace("{$placeholder2}", "value2")):
                    result = initialise_prompt(agent)
                    assert result == "This is a test prompt with value1 and value2."
                    mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
                    mock_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")

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
temp\temp.py:32: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.29s
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
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_yaml_load = {"placeholder1": "value1", "placeholder2": "value2"}
    mock_prompt_structure = "This is a test prompt with {$placeholder1} and {$placeholder2}."

    with patch("builtins.open", mock_open(read_data=mock_prompt_structure)) as mock_file:
        with patch("yaml.load", return_value=mock_yaml_load):
            result = initialise_prompt(agent)
            assert result == "This is a test prompt with value1 and value2."
            mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
            mock_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")

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
temp\temp.py:32: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.30s

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

def test_initialise_prompt_file_not_found(mock_config_path):
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____________________ test_initialise_prompt_file_not_found ____________________
temp\temp.py:31: in test_initialise_prompt_file_not_found
    with patch("builtins.open", side_effect=FileNotFoundError):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_file_not_found - NameError: name ...
1 failed in 0.25s
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

from unittest.mock import patch
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
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
temp\temp.py:30: in <module>
    from your_module import initialise_prompt  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.28s
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

from unittest.mock import patch
from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_prompt_file_not_found():
    agent = "non_existent_agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
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
temp\temp.py:30: in <module>
    from your_actual_module_name import initialise_prompt  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.28s

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

def test_initialise_prompt_invalid_yaml(mock_config_path):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.load", side_effect=yaml.YAMLError):
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
_____________________ test_initialise_prompt_invalid_yaml _____________________
temp\temp.py:31: in test_initialise_prompt_invalid_yaml
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_invalid_yaml - NameError: name 'p...
1 failed in 0.16s
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

import pytest
from unittest.mock import patch, mock_open
import yaml
from your_module import initialise_prompt

def test_initialise_prompt_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.load", side_effect=yaml.YAMLError):
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
temp\temp.py:32: in <module>
    from your_module import initialise_prompt
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.31s
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

import pytest
from unittest.mock import patch, mock_open
import yaml
from source_code import initialise_prompt

def test_initialise_prompt_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.load", side_effect=yaml.YAMLError):
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
temp\temp.py:32: in <module>
    from source_code import initialise_prompt
E   ModuleNotFoundError: No module named 'source_code'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.33s

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
F                                                                        [100%]
================================== FAILURES ===================================
___________________ test_initialise_settings_file_not_found ___________________
temp\temp.py:31: in test_initialise_settings_file_not_found
    with patch("builtins.open", side_effect=FileNotFoundError):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_file_not_found - NameError: nam...
1 failed in 0.12s
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

from unittest.mock import patch
from your_module import initialise_settings

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
temp\temp.py:30: in <module>
    from your_module import initialise_settings
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

from unittest.mock import patch
from your_module import initialise_settings

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
temp\temp.py:30: in <module>
    from your_module import initialise_settings
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.16s

TEST CASE 6 Retry 0
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

def test_initialise_settings_invalid_yaml(mock_config_path):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.safe_load", side_effect=yaml.YAMLError):
            result = initialise_settings(agent)
            assert result is None

---------------
TEST CASE 6 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____________________ test_initialise_settings_invalid_yaml ____________________
temp\temp.py:31: in test_initialise_settings_invalid_yaml
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_invalid_yaml - NameError: name ...
1 failed in 0.20s
TEST CASE 6 Retry 1
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
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.safe_load", side_effect=yaml.YAMLError):
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
temp\temp.py:31: in <module>
    from your_module import initialise_settings  # Replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.25s
TEST CASE 6 Retry 2
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
from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name

def test_initialise_settings_invalid_yaml():
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data="invalid_yaml")):
        with patch("yaml.safe_load", side_effect=yaml.YAMLError):
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
temp\temp.py:31: in <module>
    from your_actual_module_name import initialise_settings  # Replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.23s
