import pytest
from uuid import UUID
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from theory_evaluation.evaluator.general_qa import (
    EvaluateTheoryPOSTRequest,
    TheoryEvaluationDeleteRequest,
    TheoryEvaluationScoreRequest,
    delete_theory_score,
    evaluate_theory,
    get_theory_score,
    process_theory_evaluation
)
from theory_evaluation.utils import (
    validate_user,
    get_marking_scheme,
    manage_user_performance,
    get_user_performance,
    delete_user_performance
)

@pytest.fixture
def mock_openai_llm():
    with patch('theory_evaluation.llm_handler.OpenAI_llm') as mock:
        yield mock

@pytest.fixture
def mock_validate_user():
    with patch('theory_evaluation.utils.validate_user') as mock:
        yield mock

@pytest.fixture
def mock_get_marking_scheme():
    with patch('theory_evaluation.utils.get_marking_scheme') as mock:
        yield mock

@pytest.fixture
def mock_manage_user_performance():
    with patch('theory_evaluation.utils.manage_user_performance') as mock:
        yield mock

@pytest.fixture
def mock_get_user_performance():
    with patch('theory_evaluation.utils.get_user_performance') as mock:
        yield mock

@pytest.fixture
def mock_delete_user_performance():
    with patch('theory_evaluation.utils.delete_user_performance') as mock:
        yield mock

def test_process_theory_evaluation_success(mock_openai_llm, mock_manage_user_performance):
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    answer = "Test answer"
    question = "Test question"
    marking_scheme = "Test marking scheme"
    model_answer = "Test model answer"

    mock_openai_llm.return_value.execute.return_value = iter([json.dumps({
        "Evaluation": "Good",
        "Score": 85,
        "Grade": "A"
    })])

    process_theory_evaluation(email, question_id, answer, question, marking_scheme, model_answer)

    mock_manage_user_performance.assert_called_with(
        mode=1,
        email=email,
        question_id=question_id,
        llm_evaluation="Good",
        llm_score=85,
        user_grade="A"
    )

def test_evaluate_theory(mock_validate_user, mock_get_marking_scheme, mock_manage_user_performance):
    client = TestClient(evaluate_theory)
    mock_validate_user.return_value = True
    mock_get_marking_scheme.return_value = ("Test question", "Test marking scheme", "Test model answer")
    mock_manage_user_performance.return_value = True

    response = client.post("/api/v1/evaluate-theory", json={
        "email": "test@example.com",
        "uuid": str(UUID("12345678-1234-5678-1234-567812345678")),
        "answer": "Test answer"
    })

    assert response.status_code == 200
    assert response.json() == {"status": "Accepted", "message": "Processing started"}

def test_get_theory_score(mock_validate_user, mock_get_marking_scheme, mock_get_user_performance):
    client = TestClient(get_theory_score)
    mock_validate_user.return_value = True
    mock_get_marking_scheme.return_value = ("Test question", "Test marking scheme", "Test model answer")
    mock_get_user_performance.return_value = (1, "Good", "A", 2)

    response = client.post("/api/v1/get-theory-score", json={
        "email": "test@example.com",
        "uuid": str(UUID("12345678-1234-5678-1234-567812345678"))
    })

    assert response.status_code == 200
    assert response.json() == {
        "user_attempts": 1,
        "evaluation": "Good",
        "grade": "A"
    }

def test_delete_theory_score(mock_validate_user, mock_delete_user_performance):
    client = TestClient(delete_theory_score)
    mock_validate_user.return_value = True
    mock_delete_user_performance.return_value = True

    response = client.post("/api/v1/delete-theory-score", json={
        "email": "test@example.com",
        "uuid": str(UUID("12345678-1234-5678-1234-567812345678"))
    })

    assert response.status_code == 204