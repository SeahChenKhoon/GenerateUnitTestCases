
TEST CASE 1 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

def test_initialise_prompt_success(mock_config_path, mock_prompt_file_content, mock_config_file_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={"name": "World"}):
            with patch("re.finditer", return_value=[re.Match("name")]):
                with patch("re.sub", return_value="Hello, World!"):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, World!"
                        mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

def test_initialise_prompt_success(mock_config_path, mock_prompt_file_content, mock_config_file_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={"name": "World"}):
            with patch("re.finditer", return_value=[re.Match("name")]):
                with patch("re.sub", return_value="Hello, World!"):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, World!"
                        mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:26: in test_initialise_prompt_success
    with patch("re.finditer", return_value=[re.Match("name")]):
E   TypeError: cannot create 're.Match' instances
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - TypeError: cannot creat...
1 failed in 0.10s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = "name: World"
    
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={"name": "World"}):
            with patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_file_content)):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace(pattern, repl)):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, World!"
                        mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = "name: World"
    
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={"name": "World"}):
            with patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_file_content)):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace(pattern, repl)):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, World!"
                        mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
TEST CASE 1 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:7: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.22s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = "name: World"
    
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={"name": "World"}):
            with patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_file_content)):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace(pattern, repl)):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, World!"
                        mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_success():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = "name: World"
    
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={"name": "World"}):
            with patch("re.finditer", return_value=re.finditer(r"\{\$(\w+)\}", mock_prompt_file_content)):
                with patch("re.sub", side_effect=lambda pattern, repl, string: string.replace(pattern, repl)):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, World!"
                        mock_file.assert_any_call(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_any_call(f"{mock_config_path}/{agent}/prompt.txt", "r")
TEST CASE 1 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:7: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s

TEST CASE 2 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

def test_initialise_prompt_missing_placeholder(mock_config_path, mock_prompt_file_content, mock_config_file_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("re.finditer", return_value=[re.Match("name")]):
                with patch("re.sub", return_value="Hello, {$name}!"):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, {$name}!"
                        mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

def test_initialise_prompt_missing_placeholder(mock_config_path, mock_prompt_file_content, mock_config_file_content):
    agent = "test_agent"
    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("re.finditer", return_value=[re.Match("name")]):
                with patch("re.sub", return_value="Hello, {$name}!"):
                    with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                        result = initialise_prompt(agent)
                        assert result == "Hello, {$name}!"
                        mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                        mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:7: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
TEST CASE 2 Retry 1
---------------
import os
import re
import yaml
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = ""

    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                result = initialise_prompt(agent)
                assert result == "Hello, {$name}!"
                mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
import os
import re
import yaml
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = ""

    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                result = initialise_prompt(agent)
                assert result == "Hello, {$name}!"
                mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml")
                mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
TEST CASE 2 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:7: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.15s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = ""

    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                result = initialise_prompt(agent)
                assert result == "Hello, {$name}!"
                mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml", "r")
                mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
---------------
import os
import re
import yaml
from unittest.mock import patch, mock_open
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_config_path():
    return "./theory_evaluation/evaluator/prompts"

@pytest.fixture
def mock_prompt_file_content():
    return "Hello, {$name}!"

@pytest.fixture
def mock_config_file_content():
    return """
    name: World
    """

@pytest.fixture
def mock_llm_settings_content():
    return """
    setting1: value1
    setting2: value2
    """

def test_initialise_prompt_missing_placeholder():
    agent = "test_agent"
    mock_config_path = "./theory_evaluation/evaluator/prompts"
    mock_prompt_file_content = "Hello, {$name}!"
    mock_config_file_content = ""

    with patch("builtins.open", mock_open(read_data=mock_config_file_content)) as mock_file:
        with patch("yaml.load", return_value={}):
            with patch("builtins.open", mock_open(read_data=mock_prompt_file_content)) as mock_prompt_file:
                result = initialise_prompt(agent)
                assert result == "Hello, {$name}!"
                mock_file.assert_called_once_with(f"{mock_config_path}/{agent}/config.yaml", "r")
                mock_prompt_file.assert_called_once_with(f"{mock_config_path}/{agent}/prompt.txt", "r")
TEST CASE 2 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:7: in <module>
    @pytest.fixture
E   NameError: name 'pytest' is not defined
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.33s
