
TEST CASE 1 Retry 0
---------------
import yaml
from theory_evaluation.llm_utils import initialise_prompt
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_filesystem():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

def test_initialise_prompt_success(mock_filesystem, mock_yaml_load):
    agent = "test_agent"
    prompt_content = "This is a {$placeholder} test."
    mock_filesystem().read.side_effect = [yaml.dump({"placeholder": "value"}), prompt_content]
    result = initialise_prompt(agent)
    assert result == "This is a value test."
    mock_filesystem.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml")
    mock_filesystem.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt")
---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:21: in test_initialise_prompt_success
    assert result == "This is a value test."
E   AssertionError: assert 'placeholder: value\n' == 'This is a value test.'
E     
E     - This is a value test.
E     + placeholder: value
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - AssertionError: assert ...
1 failed in 0.10s
TEST CASE 1 Retry 1
---------------
import os
import yaml
from theory_evaluation.llm_utils import initialise_prompt
import pytest
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_filesystem():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

def test_initialise_prompt_success():
    agent = "test_agent"
    config_content = "placeholder: value\n"
    prompt_content = "This is a {$placeholder} test."
    expected_result = "This is a value test."

    with patch("builtins.open", mock_open(read_data=config_content)) as mock_file:
        with patch("yaml.load", return_value={"placeholder": "value"}):
            with patch("os.path.exists", return_value=True):
                result = initialise_prompt(agent)
                assert result == expected_result
                mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml")
                mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt")
---------------
TEST CASE 1 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:27: in test_initialise_prompt_success
    assert result == expected_result
E   AssertionError: assert 'placeholder: value\n' == 'This is a value test.'
E     
E     - This is a value test.
E     + placeholder: value
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - AssertionError: assert ...
1 failed in 0.11s
TEST CASE 1 Retry 2
---------------
import os
import yaml
import pytest
from unittest.mock import mock_open, patch
from theory_evaluation.llm_utils import initialise_prompt

@pytest.fixture
def mock_filesystem():
    with patch("builtins.open", mock_open()) as mocked_open:
        yield mocked_open

@pytest.fixture
def mock_yaml_load():
    with patch("yaml.load", return_value={"placeholder": "value"}) as mocked_yaml_load:
        yield mocked_yaml_load

@pytest.fixture
def mock_yaml_safe_load():
    with patch("yaml.safe_load", return_value={"key": "value"}) as mocked_yaml_safe_load:
        yield mocked_yaml_safe_load

def test_initialise_prompt_success():
    agent = "test_agent"
    config_content = "placeholder: value\n"
    prompt_content = "This is a {$placeholder} test."
    expected_result = "This is a value test."

    with patch("builtins.open", mock_open(read_data=prompt_content)) as mock_file:
        with patch("yaml.load", return_value={"placeholder": "value"}):
            result = initialise_prompt(agent)
            assert result == expected_result
            mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/config.yaml")
            mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt")
---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
_______________________ test_initialise_prompt_success ________________________
temp\temp.py:33: in test_initialise_prompt_success
    mock_file.assert_any_call(f"./theory_evaluation/evaluator/prompts/{agent}/prompt.txt")
C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\unittest\mock.py:1048: in assert_any_call
    raise AssertionError(
E   AssertionError: open('./theory_evaluation/evaluator/prompts/test_agent/prompt.txt') call not found
=========================== short test summary info ===========================
FAILED temp/temp.py::test_initialise_prompt_success - AssertionError: open('....
1 failed in 0.16s
