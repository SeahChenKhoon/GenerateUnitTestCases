from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Text, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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

def test_user_info_creation():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()

    user = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        github_username="johndoe",
        payment_date=None,
        current_duration=0,
        course_duration=10,
        end_date=None,
        status=1
    )
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(UserInfo).filter_by(email="john.doe@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.first_name == "John"
    assert retrieved_user.last_name == "Doe"