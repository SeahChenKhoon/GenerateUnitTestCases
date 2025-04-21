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
    func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import uuid
import pytest
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog

Base = declarative_base()

@pytest.fixture(scope='module')
def engine():
    return create_engine('sqlite:///:memory:')

@pytest.fixture(scope='module')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

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

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def test_user_info_unique_email_constraint():
    # Arrange
    user1 = UserInfo(
        first_name="John",
        last_name="Doe",
        email="unique@example.com",
        github_username="johndoe",
        payment_date=func.now(),
        current_duration=10,
        course_duration=20,
        end_date=func.now(),
        status=1
    )
    user2 = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="unique@example.com",
        github_username="janedoe",
        payment_date=func.now(),
        current_duration=15,
        course_duration=25,
        end_date=func.now(),
        status=2
    )
    
    # Act
    session.add(user1)
    session.commit()
    
    # Assert
    with pytest.raises(IntegrityError):
        session.add(user2)
        session.commit()