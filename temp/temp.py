import pytest
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Text, UniqueConstraint, ForeignKey, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

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

class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(Text)
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())

class UserRepo(Base):
    __tablename__ = "user_repo"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_info.id"), nullable=False)
    psid = Column(Integer)
    github_username = Column(String(50), nullable=False)
    repo_name = Column(String(255), nullable=False)
    github_url = Column(String(255), nullable=False)
    __table_args__ = (
        UniqueConstraint("github_username", "repo_name", name="unique_user_repo"),
    )

class Curriculum(Base):
    __tablename__ = "curriculum"
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    question = Column(Text, unique=True, nullable=False)
    marking_scheme = Column(Text, nullable=False)
    model_answer = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='module')
def db_session():
    session = Session()
    yield session
    session.close()

def test_user_info_creation(db_session):
    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"

def test_user_info_unique_email_constraint(db_session):
    user1 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        github_username="janedoe",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    user2 = UserInfo(
        first_name="Janet",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janetsmith",
        payment_date=datetime.now(),
        current_duration=5,
        course_duration=10,
        end_date=datetime.now(),
        status=1
    )
    db_session.add(user1)
    db_session.commit()
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()

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
        github_url="http://github.com/alice/repo1"
    )
    db_session.add(user_repo2)
    with pytest.raises(Exception):
        db_session.commit()

def test_curriculum_creation(db_session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness",
        model_answer="Python is a programming language."
    )
    db_session.add(curriculum)
    db_session.commit()
    retrieved_curriculum = db_session.query(Curriculum).filter_by(question="What is Python?").first()
    assert retrieved_curriculum is not None
    assert retrieved_curriculum.marking_scheme == "Correctness"