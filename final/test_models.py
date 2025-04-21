from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, ForeignKey, UniqueConstraint, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError
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
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

def test_user_repo_unique_constraint(db_session):
    user = UserInfo(
        first_name="Alice",
        last_name="Doe",
        email="alice.doe@example.com",
        github_username="alicedoe",
        payment_date=None,
        current_duration=5,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    user_repo1 = UserRepo(
        user_id=user.id,
        psid=1,
        github_username="alicedoe",
        repo_name="repo1",
        github_url="http://github.com/alicedoe/repo1"
    )
    user_repo2 = UserRepo(
        user_id=user.id,
        psid=2,
        github_username="alicedoe",
        repo_name="repo1",
        github_url="http://github.com/alicedoe/repo2"
    )
    db_session.add(user_repo1)
    db_session.commit()
    db_session.add(user_repo2)
    with pytest.raises(IntegrityError):
        db_session.commit()