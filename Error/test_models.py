
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
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
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()

---------------
TEST CASE 1 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002B34243FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002B34243FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:30:06,796 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:30:06,796 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:30:06,796 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,797 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:30:06,797 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,797 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:30:06,797 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,797 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:30:06,798 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:30:06,799 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:30:06,800 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:06,801 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:30:06,801 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 08:30:06,802 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:30:06,802 INFO sqlalchemy.engine.Engine [no key 0.00012s] ()
2025-04-21 08:30:06,803 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00011s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00012s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_creation - sqlalchemy.exc.CompileError: (i...
1 warning, 1 error in 1.29s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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
from your_module import Base, UserInfo  # replace 'your_module' with the actual module name

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_user_info_creation(db_session):
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
    db_session.add(user)
    db_session.commit()
    assert user.id is not None

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
temp\temp.py:41: in <module>
    from your_module import Base, UserInfo  # replace 'your_module' with the actual module name
E   ModuleNotFoundError: No module named 'your_module'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.11s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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
from your_actual_module_name import Base, UserInfo  # replace 'your_actual_module_name' with the actual module name

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_user_info_creation(db_session):
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
    db_session.add(user)
    db_session.commit()
    assert user.id is not None

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
temp\temp.py:41: in <module>
    from your_actual_module_name import Base, UserInfo  # replace 'your_actual_module_name' with the actual module name
E   ModuleNotFoundError: No module named 'your_actual_module_name'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.84s

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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_user_info_unique_email_constraint(db_session):
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
    db_session.add(user1)
    db_session.commit()

---------------
TEST CASE 2 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002D51664FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002D51664FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:30:21,550 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:30:21,551 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:30:21,551 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,552 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:30:21,552 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,552 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:30:21,552 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,552 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:30:21,553 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,553 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:30:21,553 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,553 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:30:21,553 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,553 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,554 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:30:21,555 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,555 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:30:21,555 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,555 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:30:21,555 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,555 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:30:21,556 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,557 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:30:21,557 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,557 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:30:21,557 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:21,558 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:30:21,558 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 08:30:21,558 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:30:21,559 INFO sqlalchemy.engine.Engine [no key 0.00013s] ()
2025-04-21 08:30:21,559 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00015s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00013s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_info_unique_email_constraint - sqlalchemy.exc.C...
1 warning, 1 error in 1.39s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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
from your_module import Base, UserInfo

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
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

def test_user_info_unique_email_constraint(db_session):
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
    db_session.add(user1)
    db_session.commit()
    
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

---------------
TEST CASE 2 Retry 1 - Result - Failed
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
temp\temp.py:41: in <module>
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
1 warning, 1 error in 0.68s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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
from your_module_name import Base, UserInfo  # Replace 'your_module_name' with the actual module name

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
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

def test_user_info_unique_email_constraint(db_session):
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
    db_session.add(user1)
    db_session.commit()
    
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

---------------
TEST CASE 2 Retry 2 - Result - Failed
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
temp\temp.py:41: in <module>
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
1 warning, 1 error in 0.94s

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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
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

---------------
TEST CASE 3 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001242E15FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001242E15FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:30:37,804 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:30:37,805 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:30:37,805 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,805 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:30:37,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,806 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:30:37,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,806 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:30:37,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:30:37,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:30:37,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,810 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:30:37,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,810 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:30:37,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,810 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:30:37,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:37,811 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:30:37,811 INFO sqlalchemy.engine.Engine [no key 0.00019s] ()
2025-04-21 08:30:37,812 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:30:37,812 INFO sqlalchemy.engine.Engine [no key 0.00016s] ()
2025-04-21 08:30:37,812 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00019s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00016s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.29s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_projects_creation(db_session):
    from sqlalchemy.dialects.postgresql import JSON
    project = Projects(
        repo_name="example_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()

---------------
TEST CASE 3 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000026FF405FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000026FF405FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:30:41,768 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:30:41,768 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:30:41,768 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,769 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:30:41,769 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,769 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:30:41,769 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:30:41,770 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,771 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:30:41,772 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:41,773 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:30:41,773 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 08:30:41,774 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:30:41,774 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 08:30:41,775 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00015s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00015s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.38s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_projects_creation(db_session):
    from sqlalchemy.dialects.postgresql import JSONB
    project = Projects(
        repo_name="example_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()

---------------
TEST CASE 3 Retry 2 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000242282CFB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000242282CFB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:30:45,386 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:30:45,387 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:30:45,387 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,388 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:30:45,388 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,388 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:30:45,389 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,389 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:30:45,389 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:30:45,390 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:30:45,391 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:30:45,392 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:45,393 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:30:45,394 INFO sqlalchemy.engine.Engine [no key 0.00021s] ()
2025-04-21 08:30:45,394 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:30:45,394 INFO sqlalchemy.engine.Engine [no key 0.00014s] ()
2025-04-21 08:30:45,395 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00021s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00014s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.26s

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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_user_repo_unique_constraint(db_session):
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
    db_session.add(user)
    db_session.commit()

---------------
TEST CASE 4 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001641169FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001641169FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:30:49,664 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:30:49,664 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:30:49,664 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,665 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:30:49,665 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,665 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:30:49,665 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,665 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:30:49,667 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,668 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:30:49,668 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,668 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:30:49,668 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,669 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:30:49,669 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,669 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:30:49,669 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,669 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:30:49,670 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:30:49,671 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,672 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:30:49,672 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,672 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:30:49,672 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:30:49,673 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:30:49,673 INFO sqlalchemy.engine.Engine [no key 0.00020s] ()
2025-04-21 08:30:49,674 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:30:49,674 INFO sqlalchemy.engine.Engine [no key 0.00016s] ()
2025-04-21 08:30:49,675 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00020s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00016s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_repo_unique_constraint - sqlalchemy.exc.Compile...
1 warning, 1 error in 1.19s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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

# Setup the database engine and session
engine = create_engine('postgresql://user:password@localhost/testdb')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_user_repo_unique_constraint(db_session):
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
    db_session.add(user)
    db_session.commit()

    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="repo1",
        github_url="http://github.com/alice/repo1"
    )
    db_session.add(user_repo1)
    db_session.commit()

    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="repo1",
        github_url="http://github.com/alice/repo2"
    )
    db_session.add(user_repo2)
    with pytest.raises(IntegrityError):
        db_session.commit()

---------------
TEST CASE 4 Retry 1 - Result - Failed
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
temp\temp.py:41: in <module>
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
1 warning, 1 error in 0.83s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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
from your_module_name import Base, UserInfo, UserRepo

# Setup the database engine and session
engine = create_engine('postgresql://user:password@localhost/testdb')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_user_repo_unique_constraint(db_session):
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
    db_session.add(user)
    db_session.commit()

    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="repo1",
        github_url="http://github.com/alice/repo1"
    )
    db_session.add(user_repo1)
    db_session.commit()

    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="repo1",
        github_url="http://github.com/alice/repo2"
    )
    db_session.add(user_repo2)
    with pytest.raises(IntegrityError):
        db_session.commit()

---------------
TEST CASE 4 Retry 2 - Result - Failed
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
temp\temp.py:41: in <module>
    from your_module_name import Base, UserInfo, UserRepo
E   ModuleNotFoundError: No module named 'your_module_name'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.64s

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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()

---------------
TEST CASE 5 Retry 0 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000200A523FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000200A523FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:31:06,359 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:31:06,359 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:31:06,360 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,360 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:31:06,360 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,360 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:31:06,360 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,360 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:31:06,361 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:31:06,362 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:31:06,363 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:06,364 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:31:06,364 INFO sqlalchemy.engine.Engine [no key 0.00013s] ()
2025-04-21 08:31:06,364 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:31:06,364 INFO sqlalchemy.engine.Engine [no key 0.00010s] ()
2025-04-21 08:31:06,365 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00013s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00010s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_curriculum_creation - sqlalchemy.exc.CompileError: (...
1 warning, 1 error in 1.36s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    assert curriculum.id is not None

---------------
TEST CASE 5 Retry 1 - Result - Failed
Test Error - c:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\unit_test_env\Lib\site-packages\pytest_asyncio\plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001D4F3D8FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001D4F3D8FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 08:31:10,062 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 08:31:10,062 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 08:31:10,062 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,063 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 08:31:10,063 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,063 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 08:31:10,064 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,064 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 08:31:10,064 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,064 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 08:31:10,064 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,064 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 08:31:10,065 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 08:31:10,066 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 08:31:10,067 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 08:31:10,068 INFO sqlalchemy.engine.Engine 
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


2025-04-21 08:31:10,068 INFO sqlalchemy.engine.Engine [no key 0.00013s] ()
2025-04-21 08:31:10,068 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 08:31:10,068 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 08:31:10,069 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00013s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00015s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_curriculum_creation - sqlalchemy.exc.CompileError: (...
1 warning, 1 error in 1.24s
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

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
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
from your_module import Base, Curriculum

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('postgresql://user:password@localhost/testdb')
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope='function')
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    assert curriculum.id is not None

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
temp\temp.py:41: in <module>
    from your_module import Base, Curriculum
E   ModuleNotFoundError: No module named 'your_module'
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.95s
