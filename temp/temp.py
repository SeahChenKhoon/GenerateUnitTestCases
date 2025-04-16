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
import pytest


# New Test Case
from sqlalchemy import inspect
from theory_evaluation.models import Curriculum

def test_curriculum_model_columns():
    inspector = inspect(Curriculum)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "question", "marking_scheme", "model_answer", "timestamp"
    ]
    assert set(columns) == set(expected_columns)
