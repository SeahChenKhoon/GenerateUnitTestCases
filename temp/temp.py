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

from models import Projects

from sqlalchemy import inspect

None

from sqlalchemy.inspection import inspect

from models import CurrentUserTable

from models import ConsultantChat

from models import MentorChat

None

from models import TheoryEvalUserPerformance


def test_theory_eval_user_performance_table_columns():
    inspector = inspect(TheoryEvalUserPerformance)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "email", "question_id", "user_response", 
        "llm_evaluation", "llm_score", "user_grade", 
        "user_attempts", "llm_evaluation_status", "timestamp"
    ]
    assert set(columns) == set(expected_columns)
