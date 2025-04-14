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
from theory_evaluation.models import ConsultantChat, CurrentUserTable, Curriculum, MentorChat, Projects, SprintIssues, TheoryEvalUserPerformance, UserInfo, UserRepo, UserScoreLog
None

None

None

None

None

None

from theory_evaluation import config

None

None

from theory_evaluation import config


def test_theory_eval_user_performance_table_columns():
    inspector = inspect(TheoryEvalUserPerformance)
    columns = inspector.columns.keys()
    expected_columns = [
        "id",
        "email",
        "question_id",
        "user_response",
        "llm_evaluation",
        "llm_score",
        "user_grade",
        "user_attempts",
        "llm_evaluation_status",
        "timestamp",
    ]
    assert set(columns) == set(expected_columns)
