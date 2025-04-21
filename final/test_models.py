from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, ForeignKey, Text, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
import pytest

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

class Curriculum(Base):
    __tablename__ = "curriculum"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    question = Column(Text, unique=True, nullable=False)
    marking_scheme = Column(Text, nullable=False)
    model_answer = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())

class TheoryEvalUserPerformance(Base):
    __tablename__ = "theory_eval_user_performance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), ForeignKey("user_info.email"))
    question_id = Column(UUID(as_uuid=True), ForeignKey("curriculum.id"))
    user_response = Column(Text)
    llm_evaluation = Column(Text)
    llm_score = Column(Float)
    user_grade = Column(String)
    user_attempts = Column(Integer)
    llm_evaluation_status = Column(Integer)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

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
    assert user.id is not None

def test_theory_eval_user_performance_creation():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = UserInfo(
        first_name="Bob",
        last_name="Builder",
        email="bob.builder@example.com",
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
        question="What is Python?",
        marking_scheme="Correct if mentions Python is a programming language.",
        model_answer="Python is a high-level programming language."
    )
    session.add(curriculum)
    session.commit()

    theory_eval = TheoryEvalUserPerformance(
        email=user.email,
        question_id=curriculum.id,
        user_response="Python is a programming language.",
        llm_evaluation="Correct",
        llm_score=1.0,
        user_grade="A",
        user_attempts=1,
        llm_evaluation_status=1
    )
    session.add(theory_eval)
    session.commit()

    assert theory_eval in session