
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
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

def test_user_info_creation(db_session):
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

---------------
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F341B6FCB0> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:22: in db_engine
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F341B6FCB0> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_creation - sqlalchemy.exc.CompileError: (i...
1 warning, 1 error in 1.32s
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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

def test_user_info_creation(db_session):
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

---------------
TEST CASE 1 Retry 1 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000023E06D7FCB0> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:22: in db_engine
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000023E06D7FCB0> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_creation - sqlalchemy.exc.CompileError: (i...
1 warning, 1 error in 1.09s
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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

# Assuming the source code is in a module named models
from models import Base, UserInfo

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine("postgresql://user:password@localhost/testdb")
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()

def test_user_info_creation(db_session):
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

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
temp\temp.py:41: in <module>
    from models import Base, UserInfo
E   ModuleNotFoundError: No module named 'models'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.97s

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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

def test_user_info_unique_email_constraint(db_session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    user2 = UserInfo(
        first_name="Jane",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janesmith",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user1)
    db_session.commit()
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

---------------
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F0BB95FCB0> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:22: in db_engine
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F0BB95FCB0> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_unique_email_constraint - sqlalchemy.exc.C...
1 warning, 1 error in 1.17s
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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from source_code import Base, UserInfo

# Assuming 'source_code' is the module where the original source code is located

# Setup an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint(db_session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    user2 = UserInfo(
        first_name="Jane",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janesmith",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user1)
    db_session.commit()
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

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
temp\temp.py:40: in <module>
    from source_code import Base, UserInfo
E   ModuleNotFoundError: No module named 'source_code'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.83s
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

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module_name import Base, UserInfo  # Replace 'your_module_name' with the actual module name

# Setup an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint(db_session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    user2 = UserInfo(
        first_name="Jane",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janesmith",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user1)
    db_session.commit()
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

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
temp\temp.py:40: in <module>
    from your_module_name import Base, UserInfo  # Replace 'your_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_module_name'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.84s

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
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

def test_projects_creation(db_session):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()
    retrieved_project = db_session.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.repo_name == "example_repo"

---------------
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001FF0A64FCB0> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:22: in db_engine
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001FF0A64FCB0> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.52s
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
import uuid
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

# Adjust the Projects class to use JSON instead of JSONB for SQLite compatibility
class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(JSON)  # Changed from JSONB to JSON
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())

# Setup an in-memory SQLite database for testing
@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(db_session):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()
    retrieved_project = db_session.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.repo_name == "example_repo"

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:42: in <module>
    class Projects(Base):
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_api.py:198: in __init__
    _as_declarative(reg, cls, dict_)
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:244: in _as_declarative
    return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:325: in setup_mapping
    return _ClassScanMapperConfig(
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:576: in __init__
    self._setup_table(table)
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:1757: in _setup_table
    table_cls(
<string>:2: in __new__
    ???
unit_test_env\Lib\site-packages\sqlalchemy\util\deprecations.py:281: in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:430: in __new__
    return cls._new(*args, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:462: in _new
    raise exc.InvalidRequestError(
E   sqlalchemy.exc.InvalidRequestError: Table 'projects' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.InvalidRequestError: Table 'projects' is ...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.14s
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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

# Use the original Projects class definition
class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(JSONB)
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())

# Setup an in-memory SQLite database for testing
@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(db_session):
    project = Projects(
        repo_name="example_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()
    retrieved_project = db_session.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.repo_name == "example_repo"

---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

=================================== ERRORS ====================================
________________________ ERROR collecting temp/temp.py ________________________
temp\temp.py:42: in <module>
    class Projects(Base):
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_api.py:198: in __init__
    _as_declarative(reg, cls, dict_)
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:244: in _as_declarative
    return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:325: in setup_mapping
    return _ClassScanMapperConfig(
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:576: in __init__
    self._setup_table(table)
unit_test_env\Lib\site-packages\sqlalchemy\orm\decl_base.py:1757: in _setup_table
    table_cls(
<string>:2: in __new__
    ???
unit_test_env\Lib\site-packages\sqlalchemy\util\deprecations.py:281: in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:430: in __new__
    return cls._new(*args, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\sql\schema.py:462: in _new
    raise exc.InvalidRequestError(
E   sqlalchemy.exc.InvalidRequestError: Table 'projects' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.InvalidRequestError: Table 'projects' is ...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.96s

TEST CASE 5 Retry 0
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

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness and efficiency",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    retrieved_curriculum = db_session.query(Curriculum).filter_by(question="What is Python?").first()
    assert retrieved_curriculum is not None
    assert retrieved_curriculum.model_answer == "Python is a programming language."

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
_________________ ERROR at setup of test_curriculum_creation __________________
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000232FE15FCB0> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:22: in db_engine
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000232FE15FCB0> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_curriculum_creation - sqlalchemy.exc.CompileError: (...
1 warning, 1 error in 1.34s
TEST CASE 5 Retry 1
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

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import CompileError
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.sqlite import JSON

# Assuming the Base and Curriculum classes are imported from the source code

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness and efficiency",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    retrieved_curriculum = db_session.query(Curriculum).filter_by(question="What is Python?").first()
    assert retrieved_curriculum is not None
    assert retrieved_curriculum.model_answer == "Python is a programming language."

---------------
TEST CASE 5 Retry 1 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000020AC1F4F770> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:48: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000020AC1F4F770> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.44s
TEST CASE 5 Retry 2
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

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.sqlite import JSON

# Assuming the Base and Curriculum classes are imported from the source code

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness and efficiency",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    retrieved_curriculum = db_session.query(Curriculum).filter_by(question="What is Python?").first()
    assert retrieved_curriculum is not None
    assert retrieved_curriculum.model_answer == "Python is a programming language."

---------------
TEST CASE 5 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002447959F770> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:46: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002447959F770> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.48s

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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

def test_theory_eval_user_performance_creation(db_session):
    user = UserInfo(
        first_name="Bob",
        last_name="Doe",
        email="bob.doe@example.com",
        github_username="bobdoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    curriculum = Curriculum(
        question="Explain SQLAlchemy.",
        marking_scheme="Detail and clarity",
        model_answer="SQLAlchemy is a SQL toolkit and ORM."
    )
    db_session.add(curriculum)
    db_session.commit()
    performance = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="SQLAlchemy is an ORM.",
        llm_evaluation="Good",
        llm_score=0.9,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    db_session.add(performance)
    db_session.commit()
    retrieved_performance = db_session.query(TheoryEvalUserPerformance).filter_by(email="bob.doe@example.com").first()
    assert retrieved_performance is not None
    assert retrieved_performance.llm_score == 0.9

---------------
TEST CASE 6 Retry 0 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002B34FF0FCB0> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:22: in db_engine
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002B34FF0FCB0> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - sqlalchemy.e...
1 warning, 1 error in 1.21s
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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

# Assuming the Base and all models are already imported

@pytest.fixture
def db_session():
    engine = create_engine('postgresql://user:password@localhost/testdb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_theory_eval_user_performance_creation(db_session):
    user = UserInfo(
        first_name="Bob",
        last_name="Doe",
        email="bob.doe@example.com",
        github_username="bobdoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    curriculum = Curriculum(
        question="Explain SQLAlchemy.",
        marking_scheme="Detail and clarity",
        model_answer="SQLAlchemy is a SQL toolkit and ORM."
    )
    db_session.add(curriculum)
    db_session.commit()
    performance = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="SQLAlchemy is an ORM.",
        llm_evaluation="Good",
        llm_score=0.9,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    db_session.add(performance)
    db_session.commit()
    retrieved_performance = db_session.query(TheoryEvalUserPerformance).filter_by(email="bob.doe@example.com").first()
    assert retrieved_performance is not None
    assert retrieved_performance.llm_score == 0.9

---------------
TEST CASE 6 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
E                                                                        [100%]
=================================== ERRORS ====================================
________ ERROR at setup of test_theory_eval_user_performance_creation _________
temp\temp.py:45: in db_session
    engine = create_engine('postgresql://user:password@localhost/testdb')
<string>:2: in create_engine
    ???
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

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - ModuleNotFou...
1 warning, 1 error in 0.70s
TEST CASE 6 Retry 2
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

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    yield session
    session.remove()
    transaction.rollback()
    connection.close()

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
import psycopg2

# Assuming the Base and all models are already imported

@pytest.fixture
def db_session():
    engine = create_engine('postgresql+psycopg2://user:password@localhost/testdb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_theory_eval_user_performance_creation(db_session):
    user = UserInfo(
        first_name="Bob",
        last_name="Doe",
        email="bob.doe@example.com",
        github_username="bobdoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    curriculum = Curriculum(
        question="Explain SQLAlchemy.",
        marking_scheme="Detail and clarity",
        model_answer="SQLAlchemy is a SQL toolkit and ORM."
    )
    db_session.add(curriculum)
    db_session.commit()
    performance = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="SQLAlchemy is an ORM.",
        llm_evaluation="Good",
        llm_score=0.9,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    db_session.add(performance)
    db_session.commit()
    retrieved_performance = db_session.query(TheoryEvalUserPerformance).filter_by(email="bob.doe@example.com").first()
    assert retrieved_performance is not None
    assert retrieved_performance.llm_score == 0.9

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
temp\temp.py:40: in <module>
    import psycopg2
E   ModuleNotFoundError: No module named 'psycopg2'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.72s
