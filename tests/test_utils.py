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

def test_get_db():
    with patch('theory_evaluation.utils.SessionLocal') as mock_session:
        mock_db = MagicMock()
        mock_session.return_value = mock_db
        with get_db() as db:
            assert db == mock_db
        mock_db.close.assert_called_once()

def test_validate_user_exists():
    email = "test@example.com"
    mock_user = MagicMock()
    mock_user.email = email
    mock_user.status = 1
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.first.return_value = mock_user
        result = validate_user(email)
        assert result is True

def test_validate_user_not_exists():
    email = "test@example.com"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.first.return_value = None
        result = validate_user(email)
        assert result is False

def test_validate_user_operational_error():
    email = "test@example.com"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.side_effect = OperationalError("error", None, None)
        result = validate_user(email)
        assert result is None

def test_get_marking_scheme_exists():
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_curriculum = MagicMock()
    mock_curriculum.question = "question"
    mock_curriculum.marking_scheme = "scheme"
    mock_curriculum.model_answer = "answer"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.first.return_value = mock_curriculum
        result = get_marking_scheme(uuid)
        assert result == ("question", "scheme", "answer")

def test_get_marking_scheme_not_exists():
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.first.return_value = None
        result = get_marking_scheme(uuid)
        assert result == (None, None, None)

def test_get_user_performance_exists():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "evaluation"
    mock_performance.user_grade = "grade"
    mock_performance.llm_evaluation_status = 2
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        result = get_user_performance(email, question_id)
        assert result == (1, "evaluation", "grade", 2)

def test_get_user_performance_not_exists():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    default_response = (0, "An unexpected error occurred. Please try again.", "No grade available.", 0)
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
        result = get_user_performance(email, question_id)
        assert result == default_response

def test_manage_user_performance_mode_0():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    user_response = "response"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
        result = manage_user_performance(0, email, question_id, user_response=user_response)
        assert result is True

def test_manage_user_performance_mode_1():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    llm_evaluation = "evaluation"
    llm_score = 10
    user_grade = "Pass"
    mock_performance = MagicMock()
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        result = manage_user_performance(1, email, question_id, llm_evaluation=llm_evaluation, llm_score=llm_score, user_grade=user_grade)
        assert result is True

def test_manage_user_performance_mode_2():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        result = manage_user_performance(2, email, question_id)
        assert result is True

def test_delete_user_performance_exists():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    mock_performance = [MagicMock(), MagicMock()]
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.all.return_value = mock_performance
        result = delete_user_performance(email, question_id)
        assert result is True

def test_delete_user_performance_not_exists():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_db
        mock_db.query.return_value.filter.return_value.all.return_value = []
        result = delete_user_performance(email, question_id)
        assert result is False