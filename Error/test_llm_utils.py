
TEST CASE 1 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

def test_initialise_prompt(agent, config_content, prompt_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"
    m = mock_open(read_data=config_content)

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.60s
TEST CASE 1 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

import pytest
from unittest.mock import mock_open, patch
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt():
    agent = "test_agent"
    config_content = "placeholder_value: test_value"
    prompt_content = "This is a {$placeholder_value} test."
    expected_output = "This is a test_value test."

    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("your_module.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
            result = initialise_prompt(agent)
            assert result == expected_output
            mock_file.assert_called_with(config_path)
            mock_prompt_file.assert_called_with(prompt_path, "r")

---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.43s
TEST CASE 1 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

import pytest
from unittest.mock import mock_open, patch
from your_module import initialise_prompt  # Replace 'your_module' with the actual module name

def test_initialise_prompt():
    agent = "test_agent"
    config_content = "placeholder_value: test_value"
    prompt_content = "This is a {$placeholder_value} test."
    expected_output = "This is a test_value test."

    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml"
    prompt_path = f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt"

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_prompt_file:
            result = initialise_prompt(agent)
            assert result == expected_output
            mock_file.assert_called_with(config_path)
            mock_prompt_file.assert_called_with(prompt_path, "r")

---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.36s

TEST CASE 2 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

def test_initialise_prompt_no_config_path():
    agent = "agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.38s
TEST CASE 2 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

from unittest.mock import patch
from your_module import initialise_prompt

def test_initialise_prompt_no_config_path():
    agent = "agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None  # Assuming the function returns None on failure

---------------
TEST CASE 2 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.32s
TEST CASE 2 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

from unittest.mock import patch
from your_module import initialise_prompt

def test_initialise_prompt_no_config_path():
    agent = "agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_prompt(agent)
        assert result is None  # Assuming the function returns None on failure

---------------
TEST CASE 2 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.27s

TEST CASE 3 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

def test_initialise_settings(agent, settings_content, expected_output):
    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
    m = mock_open(read_data=settings_content)

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.46s
TEST CASE 3 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

import pytest
from unittest.mock import mock_open, patch
import yaml
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings():
    agent = "test_agent"
    settings_content = """
    key1: value1
    key2: value2
    """
    expected_output = {
        "key1": "value1",
        "key2": "value2"
    }

    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
    
    with patch("builtins.open", mock_open(read_data=settings_content)):
        with patch("yaml.safe_load", return_value=expected_output):
            result = initialise_settings(agent)
            assert result == expected_output

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.39s
TEST CASE 3 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

import pytest
from unittest.mock import mock_open, patch
import yaml
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings():
    agent = "test_agent"
    settings_content = """
    key1: value1
    key2: value2
    """
    expected_output = {
        "key1": "value1",
        "key2": "value2"
    }

    config_path = f"./theory_evaluation/evaluator/prompts/{agent}/llm_settings.yaml"
    
    with patch("builtins.open", mock_open(read_data=settings_content)):
        result = initialise_settings(agent)
        assert result == expected_output

---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.56s

TEST CASE 4 Retry 0
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

def test_initialise_settings_no_config_path():
    agent = "agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.33s
TEST CASE 4 Retry 1
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

import pytest
from unittest.mock import patch
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_no_config_path():
    agent = "agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 4 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.33s
TEST CASE 4 Retry 2
---------------
import os
import re
import yaml
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings
import pytest

There are no `@pytest.fixture` functions in the provided unit test file.

import pytest
from unittest.mock import patch
from your_module import initialise_settings  # Replace 'your_module' with the actual module name

def test_initialise_settings_no_config_path():
    agent = "agent"
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = initialise_settings(agent)
        assert result is None

---------------
TEST CASE 4 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\_pytest\python.py:493: in importtestmodule
    mod = import_path(
unit_test_env\Lib\site-packages\_pytest\pathlib.py:587: in import_path
    importlib.import_module(module_name)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:176: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
unit_test_env\Lib\site-packages\_pytest\assertion\rewrite.py:356: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\ast.py:54: in parse
    return compile(source, filename, mode, flags,
E     File "C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py", line 7
E       There are no `@pytest.fixture` functions in the provided unit test file.
E             ^^^
E   SyntaxError: invalid syntax
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.25s
