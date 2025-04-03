import pytest
from unittest.mock import patch, MagicMock
from uuid import UUID
from sqlalchemy.exc import OperationalError, SQLAlchemyError
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
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.UserInfo') as mock_user_info:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = mock_user
        result = validate_user(email)
        assert result is True

def test_validate_user_not_exists():
    email = "test@example.com"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None
        result = validate_user(email)
        assert result is False

def test_validate_user_operational_error():
    email = "test@example.com"
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.side_effect = OperationalError("Error", "params", "orig")
        result = validate_user(email)
        assert result is None

def test_get_marking_scheme_success():
    uuid = UUID("12345678123456781234567812345678")
    mock_curriculum = MagicMock()
    mock_curriculum.question = "Question"
    mock_curriculum.marking_scheme = "Scheme"
    mock_curriculum.model_answer = "Answer"
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.Curriculum') as mock_curriculum_model:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = mock_curriculum
        question, scheme, answer = get_marking_scheme(uuid)
        assert question == "Question"
        assert scheme == "Scheme"
        assert answer == "Answer"

def test_get_marking_scheme_operational_error():
    uuid = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.side_effect = OperationalError("Error", "params", "orig")
        question, scheme, answer = get_marking_scheme(uuid)
        assert question is None
        assert scheme is None
        assert answer is None

def test_get_user_performance_success():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    mock_performance.llm_evaluation = "Evaluation"
    mock_performance.user_grade = "Grade"
    mock_performance.llm_evaluation_status = 1
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.TheoryEvalUserPerformance') as mock_performance_model:
        mock_get_db.return_value.__enter__.return_value.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        attempts, evaluation, grade, status = get_user_performance(email, question_id)
        assert attempts == 1
        assert evaluation == "Evaluation"
        assert grade == "Grade"
        assert status == 1

def test_get_user_performance_operational_error():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.side_effect = OperationalError("Error", "params", "orig")
        attempts, evaluation, grade, status = get_user_performance(email, question_id)
        assert attempts == 0
        assert evaluation == "An unexpected error occurred. Please try again."
        assert grade == "No grade available."
        assert status == 0

def test_manage_user_performance_mode_0_success():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    user_response = "Response"
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.TheoryEvalUserPerformance') as mock_performance_model:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
        result = manage_user_performance(0, email, question_id, user_response=user_response)
        assert result is True

def test_manage_user_performance_mode_1_success():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    llm_evaluation = "Evaluation"
    llm_score = 90
    user_grade = "Pass"
    mock_performance = MagicMock()
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.TheoryEvalUserPerformance') as mock_performance_model:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        result = manage_user_performance(1, email, question_id, llm_evaluation=llm_evaluation, llm_score=llm_score, user_grade=user_grade)
        assert result is True

def test_manage_user_performance_mode_2_success():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    mock_performance = MagicMock()
    mock_performance.user_attempts = 1
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.TheoryEvalUserPerformance') as mock_performance_model:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.order_by.return_value.first.return_value = mock_performance
        result = manage_user_performance(2, email, question_id)
        assert result is True

def test_delete_user_performance_success():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    mock_performance = MagicMock()
    with patch('theory_evaluation.utils.get_db') as mock_get_db, \
         patch('theory_evaluation.utils.models.TheoryEvalUserPerformance') as mock_performance_model:
        mock_db = mock_get_db.return_value.__enter__.return_value
        mock_db.query.return_value.filter.return_value.all.return_value = [mock_performance]
        result = delete_user_performance(email, question_id)
        assert result is True

def test_delete_user_performance_operational_error():
    email = "test@example.com"
    question_id = UUID("12345678123456781234567812345678")
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_get_db.return_value.__enter__.side_effect = OperationalError("Error", "params", "orig")
        result = delete_user_performance(email, question_id)
        assert result is False