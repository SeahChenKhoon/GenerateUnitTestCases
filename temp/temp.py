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
from theory_evaluation.models import Base, UserInfo, UserRepo
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope="module")
def engine():
    return create_engine(TEST_DATABASE_URL)

@pytest.fixture(scope="function")
def session(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(engine)

def test_user_repo_unique_constraint(session):
    user_info = UserInfo(
        first_name="Alice",
        last_name="Johnson",
        email="alice.johnson@example.com",
        github_username="alicejohnson",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    session.add(user_info)
    session.commit()
    user_repo1 = UserRepo(
        user_id=user_info.id,
        psid=1,
        github_username="alicejohnson",
        repo_name="repo1",
        github_url="http://github.com/alicejohnson/repo1"
    )
    user_repo2 = UserRepo(
        user_id=user_info.id,
        psid=2,
        github_username="alicejohnson",
        repo_name="repo1",
        github_url="http://github.com/alicejohnson/repo2"
    )
    session.add(user_repo1)
    session.commit()
    with pytest.raises(IntegrityError):
        session.add(user_repo2)
        session.commit()