
TEST CASE 2 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_prompt_raises_value_error_on_missing_config_path():
    agent = "test_agent"
    config_path = None
    with patch("builtins.open", mock_open()), patch("yaml.load", return_value={}):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_prompt(agent)

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
______ test_initialise_prompt_raises_value_error_on_missing_config_path _______
temp\temp.py:12: in test_initialise_prompt_raises_value_error_on_missing_config_path
    with patch("builtins.open", mock_open()), patch("yaml.load", return_value={}):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_raises_value_error_on_missing_config_path
1 failed in 0.21s
TEST CASE 2 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_prompt_raises_value_error_on_missing_config_path():
    agent = "test_agent"
    config_path = None
    with patch("builtins.open", mock_open()), patch("yaml.load", return_value={}):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_prompt(agent)

---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
______ test_initialise_prompt_raises_value_error_on_missing_config_path _______
temp\temp.py:16: in test_initialise_prompt_raises_value_error_on_missing_config_path
    with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_raises_value_error_on_missing_config_path
1 failed in 0.18s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_prompt_raises_value_error_on_missing_config_path():
    agent = "test_agent"
    with patch("builtins.open", mock_open()), patch("yaml.load", return_value={}):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_prompt(agent)

---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
______ test_initialise_prompt_raises_value_error_on_missing_config_path _______
temp\temp.py:15: in test_initialise_prompt_raises_value_error_on_missing_config_path
    with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_raises_value_error_on_missing_config_path
1 failed in 0.21s

TEST CASE 6 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_settings_raises_value_error_on_missing_config_path():
    agent = "test_agent"
    config_path = None
    with patch("builtins.open", mock_open()), patch("yaml.safe_load", return_value={}):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_settings(agent)

---------------
TEST CASE 6 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_____ test_initialise_settings_raises_value_error_on_missing_config_path ______
temp\temp.py:12: in test_initialise_settings_raises_value_error_on_missing_config_path
    with patch("builtins.open", mock_open()), patch("yaml.safe_load", return_value={}):
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_raises_value_error_on_missing_config_path
1 failed in 0.15s
TEST CASE 6 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open
from your_module_name import initialise_settings  # Replace with the actual module name

def test_initialise_settings_raises_value_error_on_missing_config_path():
    agent = "test_agent"
    with patch("builtins.open", mock_open()), patch("yaml.safe_load", return_value={}):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_settings(agent)

---------------
TEST CASE 6 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:11: in <module>
    from your_module_name import initialise_settings  # Replace with the actual module name
E   ModuleNotFoundError: No module named 'your_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.20s
TEST CASE 6 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open
from your_actual_module_name import initialise_settings  # Replace with the actual module name

def test_initialise_settings_raises_value_error_on_missing_config_path():
    agent = "test_agent"
    with patch("builtins.open", mock_open()), patch("yaml.safe_load", return_value={}):
        with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
            initialise_settings(agent)

---------------
TEST CASE 6 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
ImportError while importing test module 'C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
temp\temp.py:11: in <module>
    from your_actual_module_name import initialise_settings  # Replace with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
