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
from sqlalchemy import inspect

def test_user_info_table_columns():
    inspector = inspect(UserInfo)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "first_name", "last_name", "email", "github_username",
        "payment_date", "current_duration", "course_duration",
        "end_date", "status"
    ]
    assert set(columns) == set(expected_columns)

def test_projects_table_columns():
    inspector = inspect(Projects)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "repo_name", "problem_statement", "bloblink",
        "mini_project_flag", "ctime"
    ]
    assert set(columns) == set(expected_columns)

def test_sprint_issues_table_columns():
    inspector = inspect(SprintIssues)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "psid", "sprint_no", "issue_no", "title",
        "description", "max_evaluations", "last_issue_flag"
    ]
    assert set(columns) == set(expected_columns)

def test_user_repo_table_columns():
    inspector = inspect(UserRepo)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "user_id", "psid", "github_username",
        "repo_name", "github_url"
    ]
    assert set(columns) == set(expected_columns)

def test_user_score_log_table_columns():
    inspector = inspect(UserScoreLog)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "user_id", "psid", "eval_sprint", "eval_issue",
        "stage", "score_number", "score_status", "current_sprint",
        "current_issue", "num_tries", "max_tries", "ctime"
    ]
    assert set(columns) == set(expected_columns)

def test_current_user_table_columns():
    inspector = inspect(CurrentUserTable)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "user_id", "psid", "current_sprint",
        "current_issue", "ctime", "num_tries"
    ]
    assert set(columns) == set(expected_columns)

def test_consultant_chat_table_columns():
    inspector = inspect(ConsultantChat)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "email", "consultant_history", "modified_on", "project_id"
    ]
    assert set(columns) == set(expected_columns)

def test_mentor_chat_table_columns():
    inspector = inspect(MentorChat)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "user_id", "route", "sender_type",
        "message_content", "timestamp"
    ]
    assert set(columns) == set(expected_columns)

def test_curriculum_table_columns():
    inspector = inspect(Curriculum)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "question", "marking_scheme", "model_answer", "timestamp"
    ]
    assert set(columns) == set(expected_columns)

def test_theory_eval_user_performance_table_columns():
    inspector = inspect(TheoryEvalUserPerformance)
    columns = [column.name for column in inspector.columns]
    expected_columns = [
        "id", "email", "question_id", "user_response",
        "llm_evaluation", "llm_score", "user_grade", "user_attempts",
        "llm_evaluation_status", "timestamp"
    ]
    assert set(columns) == set(expected_columns)