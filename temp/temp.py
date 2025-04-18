from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    Float,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from theory_evaluation.models import Base, ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog

@pytest.fixture
def sample_fixture():
    return {"key": "value"}

@pytest.fixture
def another_fixture():
    return [1, 2, 3]