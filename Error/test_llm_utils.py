
TEST CASE 1 Retry 0
---------------
import os
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

def test_initialise_prompt_success(mock_config_path, mock_prompt_file_content, mock_config_file_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
            with patch("os.path.exists", return_value=True):
                result = initialise_prompt(agent)
                assert result == "This is a prompt with a value."
                mock_file.assert_called_with(f"{mock_config_path}/{agent}/config.yaml")
                mock_prompt_file.assert_called_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
TEST CASE 1 Retry 0 - Result - Failed
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
1 error in 0.25s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
import pytest
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "This is a prompt with a {$value}."
    mock_config_file_content = "value: value"

    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
            result = initialise_prompt(agent)
            assert result == "This is a prompt with a value."
            mock_file.assert_called_with(f"{mock_config_path}/{agent}/config.yaml")
            mock_prompt_file.assert_called_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:38: in test_initialise_prompt_success
    assert result == "This is a prompt with a value."
E   AssertionError: assert None == 'This is a prompt with a value.'
---------------------------- Captured stdout call -----------------------------
string indices must be integers, not 'str': No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - AssertionError: assert ...
1 failed in 0.24s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
import pytest
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "This is a prompt with a {$value}."
    mock_config_file_content = "value: value"

    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
        with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
            result = initialise_prompt(agent)
            assert result == "This is a prompt with a value."
            mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
            mock_prompt_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:38: in test_initialise_prompt_success
    assert result == "This is a prompt with a value."
E   AssertionError: assert 'value: value' == 'This is a pr...with a value.'
E     
E     - This is a prompt with a value.
E     + value: value
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - AssertionError: assert ...
1 failed in 0.25s

TEST CASE 2 Retry 0
---------------
import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

def test_initialise_prompt_missing_placeholder(mock_config_path, mock_prompt_file_content):
    agent = "test_agent"
    incomplete_config_content = """
    another_placeholder: "value"
    """
    with patch("builtins.open", mock_open(read_data=incomplete_config_content)) as mock_file:
        with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
            with patch("os.path.exists", return_value=True):
                result = initialise_prompt(agent)
                assert result == "This is a prompt with a {$placeholder}."
                mock_file.assert_called_with(f"{mock_config_path}/{agent}/config.yaml")
                mock_prompt_file.assert_called_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_________________ test_initialise_prompt_missing_placeholder __________________
temp\temp.py:24: in test_initialise_prompt_missing_placeholder
    assert result == "This is a prompt with a {$placeholder}."
E   AssertionError: assert None == 'This is a prompt with a {$placeholder}.'
---------------------------- Captured stdout call -----------------------------
string indices must be integers, not 'str': No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_missing_placeholder - AssertionEr...
1 failed in 0.25s
TEST CASE 2 Retry 1
---------------
import os
import pytest
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    incomplete_config_content = """
    another_placeholder: "value"
    """
    mock_prompt_file_content = "This is a prompt with a {$placeholder}."
    
    with patch("builtins.open", mock_open(read_data=incomplete_config_content)) as mock_file:
        with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
            with patch("os.path.exists", return_value=True):
                result = initialise_prompt(agent)
                assert result == "This is a prompt with a {$placeholder}."
                mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
                mock_prompt_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_________________ test_initialise_prompt_missing_placeholder __________________
temp\temp.py:39: in test_initialise_prompt_missing_placeholder
    assert result == "This is a prompt with a {$placeholder}."
E   AssertionError: assert None == 'This is a prompt with a {$placeholder}.'
---------------------------- Captured stdout call -----------------------------
string indices must be integers, not 'str': No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_missing_placeholder - AssertionEr...
1 failed in 0.23s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
import pytest
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "This is a prompt with a {$placeholder}."

@pytest.fixture
def mock_config_file_content():
    return """
    placeholder: "value"
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: "value1"
    setting2: "value2"
    """

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    incomplete_config_content = """
    another_placeholder: "value"
    """
    mock_prompt_file_content = "This is a prompt with a {$placeholder}."
    
    with patch("builtins.open", mock_open(read_data=incomplete_config_content)) as mock_file:
        with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
            result = initialise_prompt(agent)
            assert result == "This is a prompt with a {$placeholder}."
            mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
            mock_prompt_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_________________ test_initialise_prompt_missing_placeholder __________________
temp\temp.py:40: in test_initialise_prompt_missing_placeholder
    assert result == "This is a prompt with a {$placeholder}."
E   AssertionError: assert None == 'This is a prompt with a {$placeholder}.'
---------------------------- Captured stdout call -----------------------------
string indices must be integers, not 'str': No configuration path to the prompt given.
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_missing_placeholder - AssertionEr...
1 failed in 0.21s
