
TEST CASE 1 Retry 0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from theory_evaluation.models import Base, UserInfo

import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_info_creation(test_db):
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info)
    test_db.commit()
    retrieved_user = test_db.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from theory_evaluation.models import Base, UserInfo

import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_info_creation(test_db):
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info)
    test_db.commit()
    retrieved_user = test_db.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"
TEST CASE 1 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________________ ERROR at setup of test_user_info_creation __________________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000147AECC3B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:23: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000147AECC3B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_creation - sqlalchemy.exc.CompileError: (i...
1 warning, 1 error in 1.07s
TEST CASE 1 Retry 1
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_creation():
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info)
    test_db.commit()
    retrieved_user = test_db.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

test_user_info_creation()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_creation():
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info)
    test_db.commit()
    retrieved_user = test_db.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

test_user_info_creation()
TEST CASE 1 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:19: in <module>
    @pytest.fixture(scope='module')
E   NameError: name 'pytest' is not defined
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.70s
TEST CASE 1 Retry 2
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_creation():
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info)
    test_db.commit()
    retrieved_user = test_db.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

test_user_info_creation()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_creation():
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info)
    test_db.commit()
    retrieved_user = test_db.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

test_user_info_creation()
TEST CASE 1 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:19: in <module>
    @pytest.fixture(scope='module')
E   NameError: name 'pytest' is not defined
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.71s

TEST CASE 2 Retry 0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint(test_db):
    user_info_1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    user_info_2 = UserInfo(
        first_name="Jake",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="jakesmith",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info_1)
    test_db.commit()
    test_db.add(user_info_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint(test_db):
    user_info_1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    user_info_2 = UserInfo(
        first_name="Jake",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="jakesmith",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info_1)
    test_db.commit()
    test_db.add(user_info_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
TEST CASE 2 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________ ERROR at setup of test_user_info_unique_email_constraint ___________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000282F57D3B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:24: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000282F57D3B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_unique_email_constraint - sqlalchemy.exc.C...
1 warning, 1 error in 1.19s
TEST CASE 2 Retry 1
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# Setup the test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_unique_email_constraint():
    user_info_1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    user_info_2 = UserInfo(
        first_name="Jake",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="jakesmith",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info_1)
    test_db.commit()
    test_db.add(user_info_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserInfo
import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# Setup the test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_unique_email_constraint():
    user_info_1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    user_info_2 = UserInfo(
        first_name="Jake",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="jakesmith",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info_1)
    test_db.commit()
    test_db.add(user_info_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
TEST CASE 2 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001FB4D343620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:32: in <module>
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001FB4D343620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.08s
TEST CASE 2 Retry 2
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    github_username = Column(String(50), nullable=False)
    payment_date = Column(TIMESTAMP(timezone=True))
    current_duration = Column(Integer)
    course_duration = Column(Integer)
    end_date = Column(TIMESTAMP(timezone=True))
    status = Column(Integer)

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

engine = create_engine('postgresql://user:password@localhost/test_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_unique_email_constraint():
    user_info_1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    user_info_2 = UserInfo(
        first_name="Jake",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="jakesmith",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info_1)
    test_db.commit()
    test_db.add(user_info_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    github_username = Column(String(50), nullable=False)
    payment_date = Column(TIMESTAMP(timezone=True))
    current_duration = Column(Integer)
    course_duration = Column(Integer)
    end_date = Column(TIMESTAMP(timezone=True))
    status = Column(Integer)

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

engine = create_engine('postgresql://user:password@localhost/test_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
test_db = Session()

def test_user_info_unique_email_constraint():
    user_info_1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    user_info_2 = UserInfo(
        first_name="Jake",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="jakesmith",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    test_db.add(user_info_1)
    test_db.commit()
    test_db.add(user_info_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
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
temp\temp.py:45: in <module>
    engine = create_engine('postgresql://user:password@localhost/test_db')
unit_test_env\Lib\site-packages\sqlalchemy\util\deprecations.py:281: in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
unit_test_env\Lib\site-packages\sqlalchemy\engine\create.py:602: in create_engine
    dbapi = dbapi_meth(**dbapi_args)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\postgresql\psycopg2.py:696: in import_dbapi
    import psycopg2
E   ModuleNotFoundError: No module named 'psycopg2'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

temp\temp.py:21
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:21: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
2 warnings, 1 error in 0.62s

TEST CASE 3 Retry 0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from theory_evaluation.models import Base, Projects

import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(test_db):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"problem": "Solve X"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    test_db.add(project)
    test_db.commit()
    retrieved_project = test_db.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"problem": "Solve X"}
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from theory_evaluation.models import Base, Projects

import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(test_db):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"problem": "Solve X"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    test_db.add(project)
    test_db.commit()
    retrieved_project = test_db.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"problem": "Solve X"}
TEST CASE 3 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________________ ERROR at setup of test_projects_creation ___________________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001616F3A3B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:23: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001616F3A3B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.08s
TEST CASE 3 Retry 1
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from theory_evaluation.models import Base, Projects

import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(test_db):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"problem": "Solve X"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    test_db.add(project)
    test_db.commit()
    retrieved_project = test_db.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"problem": "Solve X"}
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from theory_evaluation.models import Base, Projects

import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(test_db):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"problem": "Solve X"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    test_db.add(project)
    test_db.commit()
    retrieved_project = test_db.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"problem": "Solve X"}
TEST CASE 3 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________________ ERROR at setup of test_projects_creation ___________________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000255C1713B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:23: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000255C1713B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.31s
TEST CASE 3 Retry 2
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, Projects
from sqlalchemy.orm import sessionmaker
import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(test_db):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"problem": "Solve X"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    test_db.add(project)
    test_db.commit()
    retrieved_project = test_db.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"problem": "Solve X"}
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, Projects
from sqlalchemy.orm import sessionmaker
import pytest

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(test_db):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"problem": "Solve X"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    test_db.add(project)
    test_db.commit()
    retrieved_project = test_db.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"problem": "Solve X"}
TEST CASE 3 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
__________________ ERROR at setup of test_projects_creation ___________________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000280CBF73B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:23: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000280CBF73B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.05s

TEST CASE 4 Retry 0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserRepo
from sqlalchemy.orm import sessionmaker
import pytest
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(test_db):
    user_repo_1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo"
    )
    user_repo_2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo2"
    )
    test_db.add(user_repo_1)
    test_db.commit()
    test_db.add(user_repo_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, UserRepo
from sqlalchemy.orm import sessionmaker
import pytest
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(test_db):
    user_repo_1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo"
    )
    user_repo_2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo2"
    )
    test_db.add(user_repo_1)
    test_db.commit()
    test_db.add(user_repo_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
TEST CASE 4 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_____________ ERROR at setup of test_user_repo_unique_constraint ______________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000149A33B3B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:24: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000149A33B3B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_repo_unique_constraint - sqlalchemy.exc.Compile...
1 warning, 1 error in 1.12s
TEST CASE 4 Retry 1
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from your_module import UserRepo

@pytest.fixture(scope='function')
def test_db():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(test_db):
    user_repo_1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo"
    )
    user_repo_2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo2"
    )
    test_db.add(user_repo_1)
    test_db.commit()
    test_db.add(user_repo_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from your_module import UserRepo

@pytest.fixture(scope='function')
def test_db():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(test_db):
    user_repo_1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo"
    )
    user_repo_2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo2"
    )
    test_db.add(user_repo_1)
    test_db.commit()
    test_db.add(user_repo_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
TEST CASE 4 Retry 1 - Result - Failed
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
temp\temp.py:20: in <module>
    from your_module import UserRepo
E   ModuleNotFoundError: No module named 'your_module'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.74s
TEST CASE 4 Retry 2
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='function')
def test_db():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(test_db):
    user_repo_1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo"
    )
    user_repo_2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo2"
    )
    test_db.add(user_repo_1)
    test_db.commit()
    test_db.add(user_repo_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='function')
def test_db():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(test_db):
    user_repo_1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo"
    )
    user_repo_2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="uniqueuser",
        repo_name="uniquerepo",
        github_url="http://github.com/uniqueuser/uniquerepo2"
    )
    test_db.add(user_repo_1)
    test_db.commit()
    test_db.add(user_repo_2)
    with pytest.raises(IntegrityError):
        test_db.commit()
    test_db.rollback()
TEST CASE 4 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_____________ ERROR at setup of test_user_repo_unique_constraint ______________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000020C8C963B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:24: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000020C8C963B60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 15:04:01,407 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 15:04:01,408 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 15:04:01,408 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,408 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 15:04:01,408 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,409 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 15:04:01,410 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,411 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 15:04:01,412 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 15:04:01,413 INFO sqlalchemy.engine.Engine 
CREATE TABLE user_info (
	id INTEGER NOT NULL, 
	first_name VARCHAR(50), 
	last_name VARCHAR(50), 
	email VARCHAR(100) NOT NULL, 
	github_username VARCHAR(50) NOT NULL, 
	payment_date TIMESTAMP, 
	current_duration INTEGER, 
	course_duration INTEGER, 
	end_date TIMESTAMP, 
	status INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (email)
)


2025-04-21 15:04:01,413 INFO sqlalchemy.engine.Engine [no key 0.00017s] ()
2025-04-21 15:04:01,413 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 15:04:01,413 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 15:04:01,414 INFO sqlalchemy.engine.Engine ROLLBACK
----------------------------- Captured log setup ------------------------------
INFO     sqlalchemy.engine.Engine:base.py:2699 BEGIN (implicit)
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("user_info")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("user_info")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("projects")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("projects")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("sprint_issues")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("sprint_issues")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("user_repo")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("user_repo")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("user_score_log")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("user_score_log")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("current_user_table")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("current_user_table")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("consultant_chat")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("consultant_chat")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("mentor_chat")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("mentor_chat")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("curriculum")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("curriculum")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("theory_eval_user_performance")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("theory_eval_user_performance")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 
CREATE TABLE user_info (
	id INTEGER NOT NULL, 
	first_name VARCHAR(50), 
	last_name VARCHAR(50), 
	email VARCHAR(100) NOT NULL, 
	github_username VARCHAR(50) NOT NULL, 
	payment_date TIMESTAMP, 
	current_duration INTEGER, 
	course_duration INTEGER, 
	end_date TIMESTAMP, 
	status INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (email)
)


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00017s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00011s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_repo_unique_constraint - sqlalchemy.exc.Compile...
1 warning, 1 error in 1.08s

TEST CASE 6 Retry 0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, TheoryEvalUserPerformance

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_theory_eval_user_performance_creation(test_db):
    theory_eval = TheoryEvalUserPerformance(
        email="john.doe@example.com",
        question_id=uuid.uuid4(),
        user_response="Python is a snake.",
        llm_evaluation="Incorrect",
        llm_score=0.0,
        user_grade="F",
        user_attempts=1,
        llm_evaluation_status=0
    )
    test_db.add(theory_eval)
    test_db.commit()
    retrieved_eval = test_db.query(TheoryEvalUserPerformance).filter_by(email="john.doe@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 0.0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, TheoryEvalUserPerformance

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_theory_eval_user_performance_creation(test_db):
    theory_eval = TheoryEvalUserPerformance(
        email="john.doe@example.com",
        question_id=uuid.uuid4(),
        user_response="Python is a snake.",
        llm_evaluation="Incorrect",
        llm_score=0.0,
        user_grade="F",
        user_attempts=1,
        llm_evaluation_status=0
    )
    test_db.add(theory_eval)
    test_db.commit()
    retrieved_eval = test_db.query(TheoryEvalUserPerformance).filter_by(email="john.doe@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 0.0
TEST CASE 6 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:18: in <module>
    @pytest.fixture(scope='module')
E   NameError: name 'pytest' is not defined
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - NameError: name 'pytest' is not defined
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.85s
TEST CASE 6 Retry 1
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, TheoryEvalUserPerformance
import pytest
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_theory_eval_user_performance_creation(test_db):
    theory_eval = TheoryEvalUserPerformance(
        email="john.doe@example.com",
        question_id=uuid.uuid4(),
        user_response="Python is a snake.",
        llm_evaluation="Incorrect",
        llm_score=0.0,
        user_grade="F",
        user_attempts=1,
        llm_evaluation_status=0
    )
    test_db.add(theory_eval)
    test_db.commit()
    retrieved_eval = test_db.query(TheoryEvalUserPerformance).filter_by(email="john.doe@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 0.0
---------------
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, TheoryEvalUserPerformance
import pytest
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_theory_eval_user_performance_creation(test_db):
    theory_eval = TheoryEvalUserPerformance(
        email="john.doe@example.com",
        question_id=uuid.uuid4(),
        user_response="Python is a snake.",
        llm_evaluation="Incorrect",
        llm_score=0.0,
        user_grade="F",
        user_attempts=1,
        llm_evaluation_status=0
    )
    test_db.add(theory_eval)
    test_db.commit()
    retrieved_eval = test_db.query(TheoryEvalUserPerformance).filter_by(email="john.doe@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 0.0
TEST CASE 6 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
________ ERROR at setup of test_theory_eval_user_performance_creation _________
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:137: in _compiler_dispatch
    meth = getter(visitor)
E   AttributeError: 'SQLiteTypeCompiler' object has no attribute 'visit_JSONB'. Did you mean: 'visit_JSON'?

The above exception was the direct cause of the following exception:
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6716: in visit_create_table
    processed = self.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6747: in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
unit_test_env\Lib\site-packages\sqlalchemy\dialects\sqlite\base.py:1598: in get_column_specification
    coltype = self.dialect.type_compiler_instance.process(
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:977: in process
    return type_._compiler_dispatch(self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:139: in _compiler_dispatch
    return visitor.visit_unsupported_compilation(self, err, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:982: in visit_unsupported_compilation
    raise exc.UnsupportedCompilationError(self, element) from err
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000017653CB3B60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:23: in test_db
    Base.metadata.create_all(engine)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:5925: in create_all
    bind._run_ddl_visitor(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:3249: in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2456: in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:981: in visit_metadata
    self.traverse_single(
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:664: in traverse_single
    return meth(obj, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:1019: in visit_table
    )._invoke_with(self.connection)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:321: in _invoke_with
    return bind.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:187: in _execute_on_connection
    return connection._execute_ddl(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1524: in _execute_ddl
    compiled = ddl.compile(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:308: in compile
    return self._compiler(dialect, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\ddl.py:76: in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:886: in __init__
    self.string = self.process(self.statement, **compile_kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:932: in process
    return obj._compiler_dispatch(self, **kwargs)
unit_test_env\Lib\site-packages\sqlalchemy\sql\visitors.py:141: in _compiler_dispatch
    return meth(self, **kw)  # type: ignore  # noqa: E501
unit_test_env\Lib\site-packages\sqlalchemy\sql\compiler.py:6726: in visit_create_table
    raise exc.CompileError(
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000017653CB3B60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - sqlalchemy.e...
1 warning, 1 error in 1.24s
TEST CASE 6 Retry 2
---------------
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.sqlite import JSON
from your_module import Projects

Projects.__table__.columns['problem_statement'].type = JSON()

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_theory_eval_user_performance_creation(test_db):
    theory_eval = TheoryEvalUserPerformance(
        email="john.doe@example.com",
        question_id=uuid.uuid4(),
        user_response="Python is a snake.",
        llm_evaluation="Incorrect",
        llm_score=0.0,
        user_grade="F",
        user_attempts=1,
        llm_evaluation_status=0
    )
    test_db.add(theory_eval)
    test_db.commit()
    retrieved_eval = test_db.query(TheoryEvalUserPerformance).filter_by(email="john.doe@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 0.0
---------------
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.sqlite import JSON
from your_module import Projects

Projects.__table__.columns['problem_statement'].type = JSON()

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_theory_eval_user_performance_creation(test_db):
    theory_eval = TheoryEvalUserPerformance(
        email="john.doe@example.com",
        question_id=uuid.uuid4(),
        user_response="Python is a snake.",
        llm_evaluation="Incorrect",
        llm_score=0.0,
        user_grade="F",
        user_attempts=1,
        llm_evaluation_status=0
    )
    test_db.add(theory_eval)
    test_db.commit()
    retrieved_eval = test_db.query(TheoryEvalUserPerformance).filter_by(email="john.doe@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 0.0
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
temp\temp.py:20: in <module>
    from your_module import Projects
E   ModuleNotFoundError: No module named 'your_module'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.67s
