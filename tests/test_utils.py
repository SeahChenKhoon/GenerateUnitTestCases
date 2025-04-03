import pytest
import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from . import models
from theory_evaluation.utils import get_db, validate_user, get_marking_scheme, get_user_performance, manage_user_performance, delete_user_performance

import pytest
from unittest.mock import patch, MagicMock
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from theory_evaluation.utils import (
    get_db,
    validate_user,
    get_marking_scheme,
    get_user_performance,
    manage_user_performance,
    delete_user_performance,
)
from pydantic import EmailStr

@pytest.fixture
def mock_db_session():
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_session = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_session
        yield mock_session

def test_validate_user_exists(mock_db_session):
    mock_user = MagicMock()
    mock_db_session.query().filter().first.return_value = mock_user
    result = validate_user(EmailStr("test@example.com"))
    assert result is True

def test_validate_user_not_exists(mock_db_session):
    mock_db_session.query().filter().first.return_value = None
    result = validate_user(EmailStr("test@example.com"))
    assert result is False

def test_validate_user_operational_error(mock_db_session):
    mock_db_session.query.side_effect = OperationalError("Test", "Test", "Test")
    result = validate_user(EmailStr("test@example.com"))
    assert result is None

def test_get_marking_scheme_success(mock_db_session):
    mock_curriculum = MagicMock()
    mock_curriculum.question = "Question"
    mock_curriculum.marking_scheme = "Scheme"
    mock_curriculum.model_answer = "Answer"
    mock_db_session.query().filter().first.return_value = mock_curriculum
    result = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert result == ("Question", "Scheme", "Answer")

def test_get_marking_scheme_failure(mock_db_session):
    mock_db_session.query().filter().first.return_value = None
    result = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert result == (None, None, None)

def test_get_user_performance_success(mock_db_session):
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "Evaluation"
    mock_performance.user_grade = "Grade"
    mock_performance.llm_evaluation_status = 1
    mock_db_session.query().filter().order_by().first.return_value = mock_performance
    result = get_user_performance(EmailStr("test@example.com"), UUID("12345678-1234-5678-1234-567812345678"))
    assert result == (1, "Evaluation", "Grade", 1)

def test_get_user_performance_default_response(mock_db_session):
    mock_db_session.query().filter().order_by().first.return_value = None
    result = get_user_performance(EmailStr("test@example.com"), UUID("12345678-1234-5678-1234-567812345678"))
    assert result == (0, "An unexpected error occurred. Please try again.", "No grade available.", 0)

def test_manage_user_performance_mode_0_success(mock_db_session):
    mock_user_performance = MagicMock()
    mock_user_performance.user_attempts = 2
    mock_user_performance.llm_evaluation = None
    mock_db_session.query().filter().order_by().first.return_value = mock_user_performance
    result = manage_user_performance(
        mode=0,
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678-1234-5678-1234-567812345678"),
        user_response="response"
    )
    assert result is True

def test_manage_user_performance_mode_1_success(mock_db_session):
    mock_user_performance = MagicMock()
    mock_db_session.query().filter().order_by().first.return_value = mock_user_performance
    result = manage_user_performance(
        mode=1,
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678-1234-5678-1234-567812345678"),
        llm_evaluation="evaluation",
        llm_score=10,
        user_grade="A"
    )
    assert result is True

def test_manage_user_performance_mode_2_success(mock_db_session):
    mock_user_performance = MagicMock()
    mock_user_performance.user_attempts = 1
    mock_db_session.query().filter().order_by().first.return_value = mock_user_performance
    result = manage_user_performance(
        mode=2,
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678-1234-5678-1234-567812345678")
    )
    assert result is True

def test_delete_user_performance_success(mock_db_session):
    mock_user_performance = [MagicMock()]
    mock_db_session.query().filter().all.return_value = mock_user_performance
    result = delete_user_performance(
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678-1234-5678-1234-567812345678")
    )
    assert result is True

def test_delete_user_performance_failure(mock_db_session):
    mock_db_session.query().filter().all.return_value = []
    result = delete_user_performance(
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678-1234-5678-1234-567812345678")
    )
    assert result is False