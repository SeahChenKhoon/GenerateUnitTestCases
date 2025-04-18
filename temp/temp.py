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

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Projects, Base  # Replace 'your_module' with the actual module name

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')  # Use an in-memory SQLite database for testing
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

def test_projects_creation(db_session):
    project = Projects(
        repo_name="test_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    db_session.add(project)
    db_session.commit()

    # Query the project back from the database to ensure it was added
    queried_project = db_session.query(Projects).filter_by(repo_name="test_repo").first()
    assert queried_project is not None
    assert queried_project.problem_statement == {"key": "value"}
    assert queried_project.bloblink == "http://example.com/blob"
    assert queried_project.mini_project_flag == 1
