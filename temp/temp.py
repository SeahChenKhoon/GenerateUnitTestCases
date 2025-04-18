from sqlalchemy import create_engine
from theory_evaluation.models import Base
import pytest
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def setup_database():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()