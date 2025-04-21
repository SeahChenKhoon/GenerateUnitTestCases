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
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

from sqlalchemy.dialects.sqlite import JSON
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module_name import Base, Projects  # Replace 'your_module_name' with the actual module name

# Adjust the Projects model to use JSON instead of JSONB for SQLite compatibility
Projects.__table__.columns.problem_statement.type = JSON()

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

def test_projects_creation():
    project = Projects(
        repo_name="test_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()
    retrieved_project = db_session.query(Projects).filter_by(repo_name="test_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"key": "value"}
