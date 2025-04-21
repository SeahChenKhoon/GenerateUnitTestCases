from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Text, UniqueConstraint, ForeignKey, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.types import JSON
from sqlalchemy.exc import IntegrityError
import pytest

Base = declarative_base()

class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    repo_name = Column(String(255), nullable=False)
    problem_statement = Column(JSON)
    bloblink = Column(Text)
    mini_project_flag = Column(Integer, nullable=False)
    ctime = Column(TIMESTAMP(timezone=True), server_default=func.now())

class UserRepo(Base):
    __tablename__ = "user_repo"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
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
def session():
    session = Session()
    yield session
    session.close()

def test_projects_creation():
    session = Session()
    project = Projects(
        repo_name="example_repo",
        problem_statement={"key": "value"},
        mini_project_flag=1
    )
    session.add(project)
    session.commit()
    retrieved_project = session.query(Projects).filter_by(repo_name="example_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.problem_statement == {"key": "value"}
    session.close()

def test_user_repo_unique_constraint(session):
    user_repo1 = UserRepo(
        user_id=1,
        psid=1,
        github_username="user1",
        repo_name="repo1",
        github_url="http://github.com/user1/repo1"
    )
    user_repo2 = UserRepo(
        user_id=2,
        psid=2,
        github_username="user1",
        repo_name="repo1",
        github_url="http://github.com/user2/repo1"
    )
    session.add(user_repo1)
    session.commit()
    session.add(user_repo2)
    with pytest.raises(IntegrityError):
        session.commit()

test_projects_creation()