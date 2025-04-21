
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_user_info_creation(session):
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    retrieved_user = session.query(UserInfo).filter_by(email="john.doe@example.com").first()
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001EF23CAFB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001EF23CAFB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_creation - sqlalchemy.exc.CompileError: (i...
1 warning, 1 error in 1.77s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Base, UserInfo

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def test_user_info_creation():
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    retrieved_user = session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

# Run the test
test_user_info_creation()

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
temp\temp.py:42: in <module>
    from your_module import Base, UserInfo
E   ModuleNotFoundError: No module named 'your_module'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.76s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP

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

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def test_user_info_creation():
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    retrieved_user = session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

# Run the test
test_user_info_creation()

---------------
TEST CASE 1 Retry 2 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
___________________________ test_user_info_creation ___________________________
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1964: in _exec_single_context
    self.dialect.do_execute(
unit_test_env\Lib\site-packages\sqlalchemy\engine\default.py:945: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: UNIQUE constraint failed: user_info.email

The above exception was the direct cause of the following exception:
temp\temp.py:79: in test_user_info_creation
    session.commit()
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:2032: in commit
    trans.commit(_to_root=True)
<string>:2: in commit
    ???
unit_test_env\Lib\site-packages\sqlalchemy\orm\state_changes.py:139: in _go
    ret_value = fn(self, *arg, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:1313: in commit
    self._prepare_impl()
<string>:2: in _prepare_impl
    ???
unit_test_env\Lib\site-packages\sqlalchemy\orm\state_changes.py:139: in _go
    ret_value = fn(self, *arg, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:1288: in _prepare_impl
    self.session.flush()
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:4353: in flush
    self._flush(objects)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:4488: in _flush
    with util.safe_reraise():
unit_test_env\Lib\site-packages\sqlalchemy\util\langhelpers.py:146: in __exit__
    raise exc_value.with_traceback(exc_tb)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:4449: in _flush
    flush_context.execute()
unit_test_env\Lib\site-packages\sqlalchemy\orm\unitofwork.py:466: in execute
    rec.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\orm\unitofwork.py:642: in execute
    util.preloaded.orm_persistence.save_obj(
unit_test_env\Lib\site-packages\sqlalchemy\orm\persistence.py:93: in save_obj
    _emit_insert_statements(
unit_test_env\Lib\site-packages\sqlalchemy\orm\persistence.py:1233: in _emit_insert_statements
    result = connection.execute(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:523: in _execute_on_connection
    return connection._execute_clauseelement(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1638: in _execute_clauseelement
    ret = self._execute_context(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1843: in _execute_context
    return self._exec_single_context(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1983: in _exec_single_context
    self._handle_dbapi_exception(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2352: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1964: in _exec_single_context
    self.dialect.do_execute(
unit_test_env\Lib\site-packages\sqlalchemy\engine\default.py:945: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user_info.email
E   [SQL: INSERT INTO user_info (first_name, last_name, email, github_username, payment_date, current_duration, course_duration, end_date, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)]
E   [parameters: ('John', 'Doe', 'john.doe@example.com', 'johndoe', None, 0, 0, None, 1)]
E   (Background on this error at: https://sqlalche.me/e/20/gkpj)
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

temp\temp.py:45
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:45: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED temp/temp.py::test_user_info_creation - sqlalchemy.exc.IntegrityError:...
1 failed, 2 warnings in 1.27s

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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_user_info_unique_email_constraint(session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    user2 = UserInfo(
        first_name="Janet",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janetsmith",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000251D53CFB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000251D53CFB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_unique_email_constraint - sqlalchemy.exc.C...
1 warning, 1 error in 1.73s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Assuming the source code is in a module named 'models'
from models import Base, UserInfo

# Setup the in-memory SQLite database
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint(session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    user2 = UserInfo(
        first_name="Janet",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janetsmith",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()

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
temp\temp.py:46: in <module>
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
1 warning, 1 error in 0.84s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint(session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    user2 = UserInfo(
        first_name="Janet",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janetsmith",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()

---------------
TEST CASE 2 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F6FEEFF620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:47: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F6FEEFF620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.34s

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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_projects_creation(session):
    project = Projects(
        repo_name="TestRepo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    session.add(project)
    session.commit()
    retrieved_project = session.query(Projects).filter_by(repo_name="TestRepo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"key": "value"}

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000296164BFB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000296164BFB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.53s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import CompileError
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(JSONB)
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())

# Setup an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
try:
    Base.metadata.create_all(engine)
except CompileError as e:
    print(f"CompileError: {e}")

def test_projects_creation():
    project = Projects(
        repo_name="TestRepo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    session.add(project)
    session.commit()
    retrieved_project = session.query(Projects).filter_by(repo_name="TestRepo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"key": "value"}

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error -
c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F                                                                        [100%]
================================== FAILURES ===================================
___________________________ test_projects_creation ____________________________
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1964: in _exec_single_context
    self.dialect.do_execute(
unit_test_env\Lib\site-packages\sqlalchemy\engine\default.py:945: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.OperationalError: no such table: projects

The above exception was the direct cause of the following exception:
temp\temp.py:78: in test_projects_creation
    session.commit()
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:2032: in commit
    trans.commit(_to_root=True)
<string>:2: in commit
    ???
unit_test_env\Lib\site-packages\sqlalchemy\orm\state_changes.py:139: in _go
    ret_value = fn(self, *arg, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:1313: in commit
    self._prepare_impl()
<string>:2: in _prepare_impl
    ???
unit_test_env\Lib\site-packages\sqlalchemy\orm\state_changes.py:139: in _go
    ret_value = fn(self, *arg, **kw)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:1288: in _prepare_impl
    self.session.flush()
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:4353: in flush
    self._flush(objects)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:4488: in _flush
    with util.safe_reraise():
unit_test_env\Lib\site-packages\sqlalchemy\util\langhelpers.py:146: in __exit__
    raise exc_value.with_traceback(exc_tb)
unit_test_env\Lib\site-packages\sqlalchemy\orm\session.py:4449: in _flush
    flush_context.execute()
unit_test_env\Lib\site-packages\sqlalchemy\orm\unitofwork.py:466: in execute
    rec.execute(self)
unit_test_env\Lib\site-packages\sqlalchemy\orm\unitofwork.py:642: in execute
    util.preloaded.orm_persistence.save_obj(
unit_test_env\Lib\site-packages\sqlalchemy\orm\persistence.py:93: in save_obj
    _emit_insert_statements(
unit_test_env\Lib\site-packages\sqlalchemy\orm\persistence.py:1233: in _emit_insert_statements
    result = connection.execute(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1416: in execute
    return meth(
unit_test_env\Lib\site-packages\sqlalchemy\sql\elements.py:523: in _execute_on_connection
    return connection._execute_clauseelement(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1638: in _execute_clauseelement
    ret = self._execute_context(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1843: in _execute_context
    return self._exec_single_context(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1983: in _exec_single_context
    self._handle_dbapi_exception(
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:2352: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
unit_test_env\Lib\site-packages\sqlalchemy\engine\base.py:1964: in _exec_single_context
    self.dialect.do_execute(
unit_test_env\Lib\site-packages\sqlalchemy\engine\default.py:945: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: projects
E   [SQL: INSERT INTO projects (repo_name, problem_statement, bloblink, mini_project_flag) VALUES (?, ?, ?, ?) RETURNING id, ctime]
E   [parameters: ('TestRepo', '{"key": "value"}', 'http://example.com/blob', 1)]
E   (Background on this error at: https://sqlalche.me/e/20/e3q8)
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

temp\temp.py:48
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:48: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED temp/temp.py::test_projects_creation - sqlalchemy.exc.OperationalError...
1 failed, 2 warnings in 1.16s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(JSONB)
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())

# Setup an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

def test_projects_creation():
    project = Projects(
        repo_name="TestRepo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    session.add(project)
    session.commit()
    retrieved_project = session.query(Projects).filter_by(repo_name="TestRepo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"key": "value"}

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])

---------------
TEST CASE 3 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002B40D94F620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:64: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002B40D94F620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

temp\temp.py:47
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\temp\temp.py:47: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
2 warnings, 1 error in 1.84s

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
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest

@pytest.fixture(scope="module")
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_user_repo_unique_constraint(session):
    user = UserInfo(
        first_name="Alice",
        last_name="Wonderland",
        email="alice@example.com",
        github_username="alice",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="Repo1",
        github_url="http://github.com/alice/repo1"
    )
    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="Repo1",
        github_url="http://github.com/alice/repo2"
    )
    session.add(user_repo1)
    session.commit()
    session.add(user_repo2)
    with pytest.raises(IntegrityError):
        session.commit()

---------------
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000186E435FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000186E435FB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_repo_unique_constraint - sqlalchemy.exc.Compile...
1 warning, 1 error in 1.45s
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

@pytest.fixture(scope="module")
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from your_module import Base, UserInfo, UserRepo

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def test_user_repo_unique_constraint():
    session = Session()
    user = UserInfo(
        first_name="Alice",
        last_name="Wonderland",
        email="alice@example.com",
        github_username="alice",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="Repo1",
        github_url="http://github.com/alice/repo1"
    )
    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="Repo1",
        github_url="http://github.com/alice/repo2"
    )
    session.add(user_repo1)
    session.commit()
    session.add(user_repo2)
    with pytest.raises(IntegrityError):
        session.commit()
    session.close()

---------------
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
temp\temp.py:44: in <module>
    from your_module import Base, UserInfo, UserRepo
E   ModuleNotFoundError: No module named 'your_module'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.00s
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

@pytest.fixture(scope="module")
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Assuming the source code is in the same module
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def test_user_repo_unique_constraint():
    session = Session()
    user = UserInfo(
        first_name="Alice",
        last_name="Wonderland",
        email="alice@example.com",
        github_username="alice",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="Repo1",
        github_url="http://github.com/alice/repo1"
    )
    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="Repo1",
        github_url="http://github.com/alice/repo2"
    )
    session.add(user_repo1)
    session.commit()
    session.add(user_repo2)
    with pytest.raises(IntegrityError):
        session.commit()
    session.close()

---------------
TEST CASE 4 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000018AEB50F620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:47: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000018AEB50F620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.63s

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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_theory_eval_user_performance_creation(session):
    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob@example.com",
        github_username="bobbuilder",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    curriculum = Curriculum(
        question="What is SQL?",
        marking_scheme="Correctness",
        model_answer="SQL is a query language."
    )
    session.add(curriculum)
    session.commit()
    performance = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="SQL is a database language.",
        llm_evaluation="Correct",
        llm_score=0.9,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    session.add(performance)
    session.commit()
    retrieved_performance = session.query(TheoryEvalUserPerformance).filter_by(email="bob@example.com").first()
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000276BBB1FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000276BBB1FB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - sqlalchemy.e...
1 warning, 1 error in 1.26s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_theory_eval_user_performance_creation(session):
    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob@example.com",
        github_username="bobbuilder",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    curriculum = Curriculum(
        question="What is SQL?",
        marking_scheme="Correctness",
        model_answer="SQL is a query language."
    )
    session.add(curriculum)
    session.commit()
    performance = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="SQL is a database language.",
        llm_evaluation="Correct",
        llm_score=0.9,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    session.add(performance)
    session.commit()
    retrieved_performance = session.query(TheoryEvalUserPerformance).filter_by(email="bob@example.com").first()
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001FD6EF3FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001FD6EF3FB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - sqlalchemy.e...
1 warning, 1 error in 1.11s
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
def engine():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_theory_eval_user_performance_creation(session):
    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob@example.com",
        github_username="bobbuilder",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user)
    session.commit()
    curriculum = Curriculum(
        question="What is SQL?",
        marking_scheme="Correctness",
        model_answer="SQL is a query language."
    )
    session.add(curriculum)
    session.commit()
    performance = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="SQL is a database language.",
        llm_evaluation="Correct",
        llm_score=0.9,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    session.add(performance)
    session.commit()
    retrieved_performance = session.query(TheoryEvalUserPerformance).filter_by(email="bob@example.com").first()
    assert retrieved_performance is not None
    assert retrieved_performance.llm_score == 0.9

---------------
TEST CASE 6 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000015BBF8BFB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:25: in tables
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000015BBF8BFB60> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - sqlalchemy.e...
1 warning, 1 error in 1.00s
