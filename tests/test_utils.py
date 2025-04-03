import pytest
import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation.utils import get_db, validate_user, get_marking_scheme, get_user_performance, manage_user_performance, delete_user_performance
from unittest.mock import patch, MagicMock
from theory_evaluation import models

@pytest.fixture
def mock_db_session():
    with patch('theory_evaluation.utils.SessionLocal') as mock_session:
        yield mock_session

def test_get_db(mock_db_session):
    with get_db() as db:
        assert hasattr(db, 'query')
    mock_db_session.return_value.close.assert_called_once()

def test_validate_user_exists(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.first.return_value = MagicMock()
    assert validate_user("test@example.com") is True

def test_validate_user_not_exists(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.first.return_value = None
    assert validate_user("test@example.com") is False

def test_validate_user_operational_error(mock_db_session):
    mock_db_session.side_effect = OperationalError("Test", "Test", "Test")
    assert validate_user("test@example.com") is None

def test_validate_user_sqlalchemy_error(mock_db_session):
    mock_db_session.side_effect = SQLAlchemyError("Test")
    assert validate_user("test@example.com") is None

def test_get_marking_scheme_exists(mock_db_session):
    mock_curriculum = MagicMock()
    mock_curriculum.question = "Question"
    mock_curriculum.marking_scheme = "Scheme"
    mock_curriculum.model_answer = "Answer"
    mock_db_session.return_value.query.return_value.filter.return_value.first.return_value = mock_curriculum
    question, scheme, answer = get_marking_scheme(UUID("12345678123456781234567812345678"))
    assert question == "Question"
    assert scheme == "Scheme"
    assert answer == "Answer"

def test_get_marking_scheme_not_exists(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.first.return_value = None
    question, scheme, answer = get_marking_scheme(UUID("12345678123456781234567812345678"))
    assert question is None
    assert scheme is None
    assert answer is None

def test_get_user_performance_exists(mock_db_session):
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "Evaluation"
    mock_performance.user_grade = "Grade"
    mock_performance.llm_evaluation_status = 2
    mock_db_session.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    attempts, evaluation, grade, status = get_user_performance("test@example.com", UUID("12345678123456781234567812345678"))
    assert attempts == 1
    assert evaluation == "Evaluation"
    assert grade == "Grade"
    assert status == 2

def test_get_user_performance_not_exists(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
    attempts, evaluation, grade, status = get_user_performance("test@example.com", UUID("12345678123456781234567812345678"))
    assert attempts == 0
    assert evaluation == "An unexpected error occurred. Please try again."
    assert grade == "No grade available."
    assert status == 0

def test_manage_user_performance_mode_0(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
    result = manage_user_performance(0, "test@example.com", UUID("12345678123456781234567812345678"), user_response="Response")
    assert result is True

def test_manage_user_performance_mode_1(mock_db_session):
    mock_performance = MagicMock()
    mock_db_session.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    result = manage_user_performance(1, "test@example.com", UUID("12345678123456781234567812345678"), llm_evaluation="Evaluation", llm_score=90, user_grade="Pass")
    assert result is True
    assert mock_performance.llm_evaluation == "Evaluation"
    assert mock_performance.llm_score == 90
    assert mock_performance.user_grade == "Pass"

def test_manage_user_performance_mode_2(mock_db_session):
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_db_session.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
    result = manage_user_performance(2, "test@example.com", UUID("12345678123456781234567812345678"))
    assert result is True

def test_delete_user_performance_exists(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.all.return_value = [MagicMock()]
    result = delete_user_performance("test@example.com", UUID("12345678123456781234567812345678"))
    assert result is True

def test_delete_user_performance_not_exists(mock_db_session):
    mock_db_session.return_value.query.return_value.filter.return_value.all.return_value = []
    result = delete_user_performance("test@example.com", UUID("12345678123456781234567812345678"))
    assert result is False