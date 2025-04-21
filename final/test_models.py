from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytest
from sqlalchemy.exc import IntegrityError

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

@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

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

    queried_user = db_session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert queried_user is not None
    assert queried_user.first_name == "John"
    assert queried_user.last_name == "Doe"
    assert queried_user.github_username == "johndoe"
    assert queried_user.current_duration == 5
    assert queried_user.course_duration == 10
    assert queried_user.status == 1

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