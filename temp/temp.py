from sqlalchemy import (
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
import pytest

Base = declarative_base()

@pytest.fixture(scope='module')
def test_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope='function')
def session(test_engine):
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()