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
from sqlalchemy import inspect

from your_module import Projects

from your_module import SprintIssues

from your_module import UserRepo

from sqlalchemy import inspect

from your_module import CurrentUserTable

from your_module import ConsultantChat

from your_module import MentorChat

from your_module import Curriculum

from your_module import TheoryEvalUserPerformance


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
