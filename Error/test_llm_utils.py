
TEST CASE 2 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_prompt_raises_value_error_when_config_path_not_set():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.load", return_value={}):
            with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                initialise_prompt(agent)

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_____ test_initialise_prompt_raises_value_error_when_config_path_not_set ______
temp\temp.py:11: in test_initialise_prompt_raises_value_error_when_config_path_not_set
    with patch("builtins.open", mock_open()) as mock_file:
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_raises_value_error_when_config_path_not_set
1 failed in 0.14s
TEST CASE 2 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



import pytest
from unittest.mock import patch, mock_open

def test_initialise_prompt_raises_value_error_when_config_path_not_set():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.load", return_value={}):
            with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                initialise_prompt(agent)

---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_____ test_initialise_prompt_raises_value_error_when_config_path_not_set ______
temp\temp.py:16: in test_initialise_prompt_raises_value_error_when_config_path_not_set
    with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_raises_value_error_when_config_path_not_set
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

def test_initialise_prompt_raises_value_error_when_config_path_not_set():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("os.environ", {}):
                with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                    initialise_prompt(agent)

---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_____ test_initialise_prompt_raises_value_error_when_config_path_not_set ______
temp\temp.py:17: in test_initialise_prompt_raises_value_error_when_config_path_not_set
    with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_raises_value_error_when_config_path_not_set
1 failed in 0.21s

TEST CASE 5 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



def test_initialise_settings_raises_value_error_when_config_path_not_set():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.safe_load", return_value={}):
            with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                initialise_settings(agent)

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____ test_initialise_settings_raises_value_error_when_config_path_not_set _____
temp\temp.py:11: in test_initialise_settings_raises_value_error_when_config_path_not_set
    with patch("builtins.open", mock_open()) as mock_file:
E   NameError: name 'patch' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_raises_value_error_when_config_path_not_set
1 failed in 0.15s
TEST CASE 5 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



from unittest.mock import patch, mock_open
import pytest

def test_initialise_settings_raises_value_error_when_config_path_not_set():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.safe_load", return_value={}):
            with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                initialise_settings(agent)

---------------
TEST CASE 5 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____ test_initialise_settings_raises_value_error_when_config_path_not_set _____
temp\temp.py:16: in test_initialise_settings_raises_value_error_when_config_path_not_set
    with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_raises_value_error_when_config_path_not_set
1 failed in 0.12s
TEST CASE 5 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest



from unittest.mock import patch, mock_open
import pytest

def test_initialise_settings_raises_value_error_when_config_path_not_set():
    agent = "test_agent"
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("yaml.safe_load", return_value={}):
            with patch("os.path.exists", return_value=False):
                with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
                    initialise_settings(agent)

---------------
TEST CASE 5 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\.venv\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
____ test_initialise_settings_raises_value_error_when_config_path_not_set _____
temp\temp.py:17: in test_initialise_settings_raises_value_error_when_config_path_not_set
    with pytest.raises(ValueError, match="CONFIG_PATH environment variable is not set"):
E   Failed: DID NOT RAISE <class 'ValueError'>
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_settings_raises_value_error_when_config_path_not_set
1 failed in 0.19s
