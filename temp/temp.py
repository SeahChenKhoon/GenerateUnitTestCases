from sqlalchemy import create_engine
from theory_evaluation.models import Base
import pytest

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()
    yield session
    session.close()