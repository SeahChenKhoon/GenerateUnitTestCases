import pytest
from unittest.mock import patch, MagicMock
from uuid import UUID
from theory_evaluation.utils import get_db, validate_user, get_marking_scheme, get_user_performance, manage_user_performance, delete_user_performance
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import pydantic

@patch('theory_evaluation.utils.SessionLocal')
def test_get_db(mock_session):
    mock_db = MagicMock()
    mock_session.return_value = mock_db
    with get_db() as db:
        assert db == mock_db
    mock_db.close.assert_called_once()

@patch('theory_evaluation.utils.get_db')
def test_validate_user_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_user = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user

    result = validate_user("test@example.com")
    assert result is True

@patch('theory_evaluation.utils.get_db')
def test_validate_user_not_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = validate_user("test@example.com")
    assert result is False

@patch('theory_evaluation.utils.get_db', side_effect=OperationalError("error", "params", "orig"))
def test_validate_user_operational_error(mock_get_db):
    result = validate_user("test@example.com")
    assert result is None

@patch('theory_evaluation.utils.get_db', side_effect=SQLAlchemyError("error"))
def test_validate_user_sqlalchemy_error(mock_get_db):
    result = validate_user("test@example.com")
    assert result is None

@patch('theory_evaluation.utils.get_db')
def test_get_marking_scheme_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_curriculum = MagicMock()
    mock_curriculum.question = "question"
    mock_curriculum.marking_scheme = "scheme"
    mock_curriculum.model_answer = "answer"
    mock_db.query.return_value.filter.return_value.first.return_value = mock_curriculum

    question, scheme, answer = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert question == "question"
    assert scheme == "scheme"
    assert answer == "answer"

@patch('theory_evaluation.utils.get_db', side_effect=OperationalError("error", "params", "orig"))
def test_get_marking_scheme_operational_error(mock_get_db):
    question, scheme, answer = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert question is None
    assert scheme is None
    assert answer is None

@patch('theory_evaluation.utils.get_db', side_effect=SQLAlchemyError("error"))
def test_get_marking_scheme_sqlalchemy_error(mock_get_db):
    question, scheme, answer = get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678"))
    assert question is None
    assert scheme is None
    assert answer is None

@patch('theory_evaluation.utils.get_db')
def test_get_user_performance_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "evaluation"
    mock_performance.user_grade = "grade"
    mock_performance.llm_evaluation_status = 2
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance

    attempts, evaluation, grade, status = get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert attempts == 1
    assert evaluation == "evaluation"
    assert grade == "grade"
    assert status == 2

@patch('theory_evaluation.utils.get_db', side_effect=OperationalError("error", "params", "orig"))
def test_get_user_performance_operational_error(mock_get_db):
    attempts, evaluation, grade, status = get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert attempts == 0
    assert evaluation == "An unexpected error occurred. Please try again."
    assert grade == "No grade available."
    assert status == 0

@patch('theory_evaluation.utils.get_db', side_effect=SQLAlchemyError("error"))
def test_get_user_performance_sqlalchemy_error(mock_get_db):
    attempts, evaluation, grade, status = get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert attempts == 0
    assert evaluation == "An unexpected error occurred. Please try again."
    assert grade == "No grade available."
    assert status == 0

@patch('theory_evaluation.utils.get_db')
def test_manage_user_performance_mode_0(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_performance.user_attempts = 2
    mock_performance.llm_evaluation = None
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance

    result = manage_user_performance(0, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), user_response="response")
    assert result is True

@patch('theory_evaluation.utils.get_db')
def test_manage_user_performance_mode_1(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance

    result = manage_user_performance(1, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), llm_evaluation="evaluation", llm_score=10, user_grade="Pass")
    assert result is True

@patch('theory_evaluation.utils.get_db')
def test_manage_user_performance_mode_2(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance

    result = manage_user_performance(2, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert result is True

@patch('theory_evaluation.utils.get_db', side_effect=OperationalError("error", "params", "orig"))
def test_manage_user_performance_operational_error(mock_get_db):
    result = manage_user_performance(0, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), user_response="response")
    assert result is False

@patch('theory_evaluation.utils.get_db', side_effect=SQLAlchemyError("error"))
def test_manage_user_performance_sqlalchemy_error(mock_get_db):
    result = manage_user_performance(0, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), user_response="response")
    assert result is False

@patch('theory_evaluation.utils.get_db')
def test_delete_user_performance_exists(mock_get_db):
    mock_db = MagicMock()
    mock_get_db.return_value.__enter__.return_value = mock_db
    mock_performance = [MagicMock(), MagicMock()]
    mock_db.query.return_value.filter.return_value.all.return_value = mock_performance

    result = delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert result is True

@patch('theory_evaluation.utils.get_db', side_effect=OperationalError("error", "params", "orig"))
def test_delete_user_performance_operational_error(mock_get_db):
    result = delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert result is False

@patch('theory_evaluation.utils.get_db', side_effect=SQLAlchemyError("error"))
def test_delete_user_performance_sqlalchemy_error(mock_get_db):
    result = delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
    assert result is False