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

def test_theory_eval_user_performance_table_structure():
    inspector = inspect(TheoryEvalUserPerformance)
    columns = inspector.columns.keys()
    assert "id" in columns
    assert "email" in columns
    assert "question_id" in columns
    assert "user_response" in columns
    assert "llm_evaluation" in columns
    assert "llm_score" in columns
    assert "user_grade" in columns
    assert "user_attempts" in columns
    assert "llm_evaluation_status" in columns
    assert "timestamp" in columns
