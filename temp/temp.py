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

def test_user_info_table_columns():
    inspector = inspect(UserInfo)
    columns = inspector.columns.keys()
    expected_columns = [
        "id", "first_name", "last_name", "email", "github_username",
        "payment_date", "current_duration", "course_duration", "end_date", "status"
    ]
    assert set(columns) == set(expected_columns)
