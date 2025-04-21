from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Text, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
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

def test_projects_creation():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    project = Projects(
        repo_name="sample_repo",
        problem_statement={"key": "value"},
        bloblink="http://example.com/blob",
        mini_project_flag=1
    )
    session.add(project)
    session.commit()

    retrieved_project = session.query(Projects).filter_by(repo_name="sample_repo").first()
    assert retrieved_project is not None
    assert retrieved_project.repo_name == "sample_repo"
    assert retrieved_project.problem_statement == {"key": "value"}
    assert retrieved_project.bloblink == "http://example.com/blob"
    assert retrieved_project.mini_project_flag == 1