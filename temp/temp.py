from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
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

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_user_info_unique_email_constraint():
    session = Session()
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
        first_name="Jane",
        last_name="Smith",
        email="jane.doe@example.com",
        github_username="janesmith",
        payment_date=None,
        current_duration=0,
        course_duration=0,
        end_date=None,
        status=1
    )
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()
    session.close()

def test_user_repo_unique_constraint(session):
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
    session.add(user)
    session.commit()

    repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alice",
        repo_name="repo1",
        github_url="https://github.com/alice/repo1"
    )
    session.add(repo1)
    session.commit()

    repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alice",
        repo_name="repo1",
        github_url="https://github.com/alice/repo2"
    )
    session.add(repo2)
    with pytest.raises(IntegrityError):
        session.commit()