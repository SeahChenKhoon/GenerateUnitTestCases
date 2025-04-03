import pytest
import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from unittest.mock import patch, MagicMock
from theory_evaluation.utils import get_db, validate_user, get_marking_scheme, get_user_performance, manage_user_performance, delete_user_performance

@patch('theory_evaluation.utils.SessionLocal')
def test_get_db(mock_session_local):
    mock_db = MagicMock()
    mock_session_local.return_value = mock_db
    with get_db() as db:
        assert db == mock_db
    mock_db.close.assert_called_once()

@patch('theory_evaluation.utils.get_db')
def test_validate_user_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_user = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user
    assert validate_user("test@example.com") is True

@patch('theory_evaluation.utils.get_db')
def test_validate_user_not_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_db.query.return_value.filter.return_value.first.return_value = None
    assert validate_user("test@example.com") is False

@patch('theory_evaluation.utils.get_db')
def test_validate_user_operational_error(mock_get_db):
    mock_get_db.side_effect = OperationalError("mock", "mock", "mock")
    assert validate_user("test@example.com") is None

@patch('theory_evaluation.utils.get_db')
def test_get_marking_scheme_success(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_curriculum = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = mock_curriculum
    mock_curriculum.question = "question"
    mock_curriculum.marking_scheme = "scheme"
    mock_curriculum.model_answer = "answer"
    result = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert result == ("question", "scheme", "answer")

@patch('theory_evaluation.utils.get_db')
def test_get_marking_scheme_none(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_db.query.return_value.filter.return_value.first.return_value = None
    result = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert result == (None, None, None)

@patch('theory_evaluation.utils.get_db')
def test_get_user_performance_success(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "evaluation"
    mock_performance.user_grade = "grade"
    mock_performance.llm_evaluation_status = 2
    result = get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert result == (1, "evaluation", "grade", 2)

@patch('theory_evaluation.utils.get_db')
def test_get_user_performance_default_response(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
    result = get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert result == (0, "An unexpected error occurred. Please try again.", "No grade available.", 0)

@patch('theory_evaluation.utils.get_db')
def test_manage_user_performance_mode_0(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_performance.user_attempts = 2
    mock_performance.llm_evaluation = None
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    assert manage_user_performance(0, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), user_response="response") is True

@patch('theory_evaluation.utils.get_db')
def test_manage_user_performance_mode_1(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    assert manage_user_performance(1, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), llm_evaluation="evaluation", llm_score=10, user_grade="grade") is True

@patch('theory_evaluation.utils.get_db')
def test_manage_user_performance_mode_2(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    assert manage_user_performance(2, "test@example.com", UUID("12345678-1234-5678-1234-567812345678")) is True

@patch('theory_evaluation.utils.get_db')
def test_delete_user_performance_success(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = [MagicMock()]
    mock_db.query.return_value.filter.return_value.all.return_value = mock_performance
    assert delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678")) is True

@patch('theory_evaluation.utils.get_db')
def test_delete_user_performance_none(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_db.query.return_value.filter.return_value.all.return_value = []
    assert delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678")) is False