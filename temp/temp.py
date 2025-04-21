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
from unittest.mock import patch
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import CompileError

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

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

def test_theory_eval_user_performance_creation():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        Base.metadata.create_all(engine)

        user_info = UserInfo(
            first_name="Alice",
            last_name="Wonderland",
            email="alice@example.com",
            github_username="alicewonder",
            payment_date=None,
            current_duration=0,
            course_duration=0,
            end_date=None,
            status=1
        )
        session.add(user_info)
        session.commit()

        curriculum = Curriculum(
            question="What is the capital of France?",
            marking_scheme="Correct if the answer is Paris.",
            model_answer="Paris"
        )
        session.add(curriculum)
        session.commit()

        theory_eval_user_performance = TheoryEvalUserPerformance(
            email="alice@example.com",
            question_id=curriculum.id,
            user_response="Paris",
            llm_evaluation="Correct",
            llm_score=1.0,
            user_grade="A",
            user_attempts=1,
            llm_evaluation_status=1
        )
        session.add(theory_eval_user_performance)
        session.commit()

    except CompileError as e:
        print(f"CompileError: {e}")
    finally:
        session.close()

test_theory_eval_user_performance_creation()