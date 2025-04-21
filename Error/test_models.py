
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001E7E3D5FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001E7E3D5FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:44:51,471 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:44:51,472 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:44:51,472 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,472 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:44:51,472 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,473 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:44:51,473 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,473 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:44:51,475 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,475 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:44:51,475 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,475 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:44:51,475 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:44:51,476 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:44:51,477 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,478 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:44:51,478 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:51,478 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:44:51,478 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 13:44:51,479 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:44:51,479 INFO sqlalchemy.engine.Engine [no key 0.00010s] ()
2025-04-21 13:44:51,479 INFO sqlalchemy.engine.Engine ROLLBACK
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
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00010s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.25s
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

def test_projects_creation(db_session):
    project = Projects(
        repo_name="example_repo",
        problem_statement=None,
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()

---------------
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000155BB13FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000155BB13FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:44:55,800 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:44:55,801 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:44:55,801 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,802 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:44:55,802 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,802 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:44:55,802 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,802 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:44:55,805 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:44:55,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:44:55,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,808 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:44:55,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,808 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:44:55,808 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:44:55,809 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:44:55,809 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 13:44:55,809 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:44:55,809 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 13:44:55,810 INFO sqlalchemy.engine.Engine ROLLBACK
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
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00011s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_projects_creation - sqlalchemy.exc.CompileError: (in...
1 warning, 1 error in 1.07s
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Base, Projects

@pytest.fixture
def db_session():
    engine = create_engine('postgresql://user:password@localhost/testdb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_projects_creation(db_session):
    project = Projects(
        repo_name="example_repo",
        problem_statement=None,
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()
    
    retrieved_project = db_session.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.repo_name == "example_repo"
    assert retrieved_project.bloblink == "http://example.com/blob"
    assert retrieved_project.mini_project_flag == 1

---------------
TEST CASE 3 Retry 2 - Result - Failed
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
    from your_module import Base, Projects
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
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

def test_user_repo_unique_constraint(db_session):
    user = UserInfo(
        first_name="Alice",
        last_name="Wonderland",
        email="alice@example.com",
        github_username="alice",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    db_session.add(user)
    db_session.commit()

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001C9AB17FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001C9AB17FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:45:12,805 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:45:12,806 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:45:12,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,806 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:45:12,806 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,806 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:45:12,807 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,807 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:45:12,809 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,810 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:45:12,811 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:12,812 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:45:12,812 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 13:45:12,812 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:45:12,812 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 13:45:12,813 INFO sqlalchemy.engine.Engine ROLLBACK
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
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00011s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_user_repo_unique_constraint - sqlalchemy.exc.Compile...
1 warning, 1 error in 1.25s
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
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Assuming the Base and UserInfo classes are defined in the same module
# from your_module import Base, UserInfo, UserRepo

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

def test_user_repo_unique_constraint():
    user = UserInfo(
        first_name="Alice",
        last_name="Wonderland",
        email="alice@example.com",
        github_username="alice",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    db_session.add(user)
    db_session.commit()

    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="repo1",
        github_url="https://github.com/alice/repo1"
    )
    db_session.add(user_repo1)
    db_session.commit()

    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="repo1",
        github_url="https://github.com/alice/repo2"
    )
    db_session.add(user_repo2)
    
    try:
        db_session.commit()
    except IntegrityError:
        db_session.rollback()
        print("Unique constraint violation caught as expected.")

---------------
TEST CASE 4 Retry 1 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001A4AB5DF620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001A4AB5DF620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.33s
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
def db_engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

def test_user_repo_unique_constraint():
    user = UserInfo(
        first_name="Alice",
        last_name="Wonderland",
        email="alice@example.com",
        github_username="alice",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    db_session.add(user)
    db_session.commit()

    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="repo1",
        github_url="https://github.com/alice/repo1"
    )
    db_session.add(user_repo1)
    db_session.commit()

    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="repo1",
        github_url="https://github.com/alice/repo2"
    )
    db_session.add(user_repo2)
    
    try:
        db_session.commit()
    except IntegrityError:
        db_session.rollback()
        print("Unique constraint violation caught as expected.")

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000223CC60F620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:44: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x00000223CC60F620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.32s

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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Detailed explanation",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000022586B6FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000022586B6FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:45:42,234 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:45:42,234 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:45:42,234 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,235 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:45:42,235 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,235 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:45:42,235 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,236 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,238 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,239 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:45:42,240 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:42,241 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:45:42,241 INFO sqlalchemy.engine.Engine [no key 0.00018s] ()
2025-04-21 13:45:42,242 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:45:42,242 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 13:45:42,242 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00018s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00011s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_curriculum_creation - sqlalchemy.exc.CompileError: (...
1 warning, 1 error in 1.44s
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Detailed explanation",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    assert curriculum.id is not None

---------------
TEST CASE 5 Retry 1 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000015E545AFB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000015E545AFB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:45:46,460 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:45:46,460 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:45:46,460 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,461 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:45:46,461 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,461 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:45:46,461 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,461 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:45:46,463 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:45:46,464 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:45:46,465 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:45:46,466 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:46,467 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:45:46,467 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 13:45:46,467 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:45:46,467 INFO sqlalchemy.engine.Engine [no key 0.00010s] ()
2025-04-21 13:45:46,468 INFO sqlalchemy.engine.Engine ROLLBACK
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
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00010s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_curriculum_creation - sqlalchemy.exc.CompileError: (...
1 warning, 1 error in 1.30s
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Detailed explanation",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    assert curriculum.id is not None

---------------
TEST CASE 5 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000016FB816FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x0000016FB816FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:45:51,136 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:45:51,137 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:45:51,137 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,137 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:45:51,138 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,138 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:45:51,138 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,138 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:45:51,141 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,141 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:45:51,141 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,141 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:45:51,141 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,142 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:45:51,143 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:45:51,144 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,145 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:45:51,145 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,145 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:45:51,145 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,146 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:45:51,146 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:51,146 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:45:51,146 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2025-04-21 13:45:51,147 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:45:51,147 INFO sqlalchemy.engine.Engine [no key 0.00009s] ()
2025-04-21 13:45:51,147 INFO sqlalchemy.engine.Engine ROLLBACK
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
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00009s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_curriculum_creation - sqlalchemy.exc.CompileError: (...
1 warning, 1 error in 1.31s

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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

def test_theory_eval_user_performance_creation(db_session):
    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob@example.com",
        github_username="bobbuilder",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    db_session.add(user)
    db_session.commit()

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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002036DD3FB60> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000002036DD3FB60> can't render element of type JSONB
---------------------------- Captured stdout setup ----------------------------
2025-04-21 13:45:56,177 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-04-21 13:45:56,178 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_info")
2025-04-21 13:45:56,178 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,178 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_info")
2025-04-21 13:45:56,179 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,179 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("projects")
2025-04-21 13:45:56,179 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,179 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("projects")
2025-04-21 13:45:56,181 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,182 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("sprint_issues")
2025-04-21 13:45:56,182 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,182 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("sprint_issues")
2025-04-21 13:45:56,182 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,182 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_repo")
2025-04-21 13:45:56,182 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_repo")
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_score_log")
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_score_log")
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("current_user_table")
2025-04-21 13:45:56,183 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("current_user_table")
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("consultant_chat")
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("consultant_chat")
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("mentor_chat")
2025-04-21 13:45:56,184 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("mentor_chat")
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("curriculum")
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("curriculum")
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("theory_eval_user_performance")
2025-04-21 13:45:56,185 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,186 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("theory_eval_user_performance")
2025-04-21 13:45:56,186 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-04-21 13:45:56,187 INFO sqlalchemy.engine.Engine 
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


2025-04-21 13:45:56,187 INFO sqlalchemy.engine.Engine [no key 0.00024s] ()
2025-04-21 13:45:56,187 INFO sqlalchemy.engine.Engine CREATE INDEX ix_user_info_id ON user_info (id)
2025-04-21 13:45:56,187 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
2025-04-21 13:45:56,188 INFO sqlalchemy.engine.Engine ROLLBACK
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


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00024s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 CREATE INDEX ix_user_info_id ON user_info (id)
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00015s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py::test_theory_eval_user_performance_creation - sqlalchemy.e...
1 warning, 1 error in 1.19s
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Assuming the Base and UserInfo classes are already defined in the source code

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

def test_theory_eval_user_performance_creation():
    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob@example.com",
        github_username="bobbuilder",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    session.add(user)
    session.commit()

---------------
TEST CASE 6 Retry 1 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001D734FDF620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:45: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001D734FDF620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.22s
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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

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

from datetime import datetime
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

def test_theory_eval_user_performance_creation():
    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob@example.com",
        github_username="bobbuilder",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    session.add(user)
    session.commit()

    theory_eval = TheoryEvalUserPerformance(
        email="bob@example.com",
        question_id=uuid.uuid4(),
        user_response="Sample response",
        llm_evaluation="Sample evaluation",
        llm_score=85.0,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1,
        timestamp=datetime.now()
    )
    session.add(theory_eval)
    session.commit()

    retrieved_eval = session.query(TheoryEvalUserPerformance).filter_by(email="bob@example.com").first()
    assert retrieved_eval is not None
    assert retrieved_eval.llm_score == 85.0
    assert retrieved_eval.user_grade == "A"

---------------
TEST CASE 6 Retry 2 - Result - Failed
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
E   sqlalchemy.exc.UnsupportedCompilationError: Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F32F51F620> can't render element of type JSONB (Background on this error at: https://sqlalche.me/e/20/l7de)

The above exception was the direct cause of the following exception:
temp\temp.py:44: in <module>
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
E   sqlalchemy.exc.CompileError: (in table 'projects', column 'problem_statement'): Compiler <sqlalchemy.dialects.sqlite.base.SQLiteTypeCompiler object at 0x000001F32F51F620> can't render element of type JSONB
============================== warnings summary ===============================
theory_evaluation\models.py:17
  C:\ChenKhoon\JupyterNotebook\GenerateUnitTestCases\theory_evaluation\models.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR temp/temp.py - sqlalchemy.exc.CompileError: (in table 'projects', colum...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 1.23s
