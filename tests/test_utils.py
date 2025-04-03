import pytest
from unittest.mock import patch, MagicMock
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError, OperationalError
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
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = mock_user
        assert validate_user(email) is True

def test_validate_user_not_exists():
    email = "test@example.com"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None
        assert validate_user(email) is False

def test_validate_user_operational_error():
    email = "test@example.com"
    with patch('theory_evaluation.utils.get_db', side_effect=OperationalError("error", "params", "orig")):
        assert validate_user(email) is None

def test_get_marking_scheme_exists():
    uuid = UUID("12345678123456781234567812345678")
    mock_curriculum = MagicMock()
    mock_curriculum.question = "Question"
    mock_curriculum.marking_scheme = "Scheme"
    mock_curriculum.model_answer = "Answer"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = mock_curriculum
        question, scheme, answer = get_marking_scheme(uuid)
        assert question == "Question"
        assert scheme == "Scheme"
        assert answer == "Answer"

def test_get_marking_scheme_not_exists():
    uuid = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None
        question, scheme, answer = get_marking_scheme(uuid)
        assert question is None
        assert scheme is None
        assert answer is None

def test_get_user_performance_exists():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "Evaluation"
    mock_performance.user_grade = "Grade"
    mock_performance.llm_evaluation_status = 2
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        attempts, evaluation, grade, status = get_user_performance(email, question_id)
        assert attempts == 1
        assert evaluation == "Evaluation"
        assert grade == "Grade"
        assert status == 2

def test_get_user_performance_not_exists():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
        attempts, evaluation, grade, status = get_user_performance(email, question_id)
        assert attempts == 0
        assert evaluation == "An unexpected error occurred. Please try again."
        assert grade == "No grade available."
        assert status == 0

def test_manage_user_performance_mode_0():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    user_response = "Response"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
        assert manage_user_performance(0, email, question_id, user_response=user_response) is True

def test_manage_user_performance_mode_1():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    llm_evaluation = "Evaluation"
    llm_score = 10
    user_grade = "Pass"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_user_performance = MagicMock()
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_user_performance
        assert manage_user_performance(1, email, question_id, llm_evaluation=llm_evaluation, llm_score=llm_score, user_grade=user_grade) is True
        assert mock_user_performance.llm_evaluation == llm_evaluation
        assert mock_user_performance.llm_score == llm_score
        assert mock_user_performance.user_grade == user_grade

def test_manage_user_performance_mode_2():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_user_performance = MagicMock()
        mock_user_performance.user_attempts = 1
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_user_performance
        assert manage_user_performance(2, email, question_id) is True
        mock_db.delete.assert_called_once_with(mock_user_performance)

def test_delete_user_performance_exists():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    mock_user_performance = [MagicMock(), MagicMock()]
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.all.return_value = mock_user_performance
        assert delete_user_performance(email, question_id) is True
        assert mock_db.delete.call_count == len(mock_user_performance)

def test_delete_user_performance_not_exists():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.all.return_value = []
        assert delete_user_performance(email, question_id) is False