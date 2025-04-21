from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Text, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid
import pytest
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Curriculum(Base):
    __tablename__ = "curriculum"
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    question = Column(Text, unique=True, nullable=False)
    marking_scheme = Column(Text, nullable=False)
    model_answer = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_curriculum_creation(session):
    curriculum = Curriculum(
        question="What is Python?",
        marking_scheme="Correctness",
        model_answer="Python is a programming language."
    )
    session.add(curriculum)
    session.commit()
    retrieved_curriculum = session.query(Curriculum).filter_by(question="What is Python?").first()
    assert retrieved_curriculum is not None
    assert retrieved_curriculum.marking_scheme == "Correctness"
    assert retrieved_curriculum.model_answer == "Python is a programming language."