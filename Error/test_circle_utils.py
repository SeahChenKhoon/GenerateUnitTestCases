
TEST CASE 1 Retry 0
---------------
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest



def test_circle_area_positive_radius():
    radius = 5.0
    expected_area = pi * radius ** 2
    result = circle_area(radius)
    assert result == expected_area

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
______________________ test_circle_area_positive_radius _______________________
temp\temp.py:9: in test_circle_area_positive_radius
    expected_area = pi * radius ** 2
E   NameError: name 'pi' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_circle_area_positive_radius - NameError: name 'pi' ...
1 failed in 0.19s
TEST CASE 1 Retry 1
---------------
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest



import math
from source_code import circle_area

def test_circle_area_positive_radius():
    radius = 5.0
    expected_area = math.pi * radius ** 2
    result = circle_area(radius)
    assert result == expected_area

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
temp\temp.py:8: in <module>
    from source_code import circle_area
E   ModuleNotFoundError: No module named 'source_code'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.20s
TEST CASE 1 Retry 2
---------------
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest



import math
from your_module_name import circle_area  # Replace 'your_module_name' with the actual module name

def test_circle_area_positive_radius():
    radius = 5.0
    expected_area = math.pi * radius ** 2
    result = circle_area(radius)
    assert result == expected_area

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
temp\temp.py:8: in <module>
    from your_module_name import circle_area  # Replace 'your_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_module_name'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.21s

TEST CASE 5 Retry 0
---------------
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest



def test_circle_circumference_positive_radius():
    radius = 5.0
    expected_circumference = 2 * pi * radius
    result = circle_circumference(radius)
    assert result == expected_circumference

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
__________________ test_circle_circumference_positive_radius __________________
temp\temp.py:9: in test_circle_circumference_positive_radius
    expected_circumference = 2 * pi * radius
E   NameError: name 'pi' is not defined
=========================== short test summary info ===========================
FAILED temp/temp.py::test_circle_circumference_positive_radius - NameError: n...
1 failed in 0.15s
TEST CASE 5 Retry 1
---------------
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest



import math
from source_code import circle_circumference

def test_circle_circumference_positive_radius():
    radius = 5.0
    expected_circumference = 2 * math.pi * radius
    result = circle_circumference(radius)
    assert result == expected_circumference

---------------
TEST CASE 5 Retry 1 - Result - Failed
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
temp\temp.py:8: in <module>
    from source_code import circle_circumference
E   ModuleNotFoundError: No module named 'source_code'
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s
TEST CASE 5 Retry 2
---------------
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest



import math
from temp.source_code import circle_circumference

def test_circle_circumference_positive_radius():
    radius = 5.0
    expected_circumference = 2 * math.pi * radius
    result = circle_circumference(radius)
    assert result == expected_circumference

---------------
TEST CASE 5 Retry 2 - Result - Failed
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
temp\temp.py:8: in <module>
    from temp.source_code import circle_circumference
E   ModuleNotFoundError: No module named 'temp.source_code'; 'temp' is not a package
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.19s
