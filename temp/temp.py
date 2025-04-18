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
from theory_evaluation.models import ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
import pytest
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

@pytest.fixture(scope='module')
def test_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope='function')
def session(test_engine):
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()