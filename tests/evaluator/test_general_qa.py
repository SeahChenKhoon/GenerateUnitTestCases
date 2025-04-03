import pytest
from ..utils import (
    validate_user,
    get_marking_scheme,
    manage_user_performance,
    get_user_performance,
    delete_user_performance,
)
import time
import logging
import json
import pydantic
from uuid import UUID
from typing import Optional
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
import asyncio
from ..llm_handler import OpenAI_llm
from ..llm_utils import initialise_prompt, initialise_settings
from theory_evaluation.evaluator.general_qa import delete_theory_score

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from uuid import UUID
from fastapi import HTTPException
from fastapi.testclient import TestClient
from theory_evaluation.evaluator.general_qa import (
    process_theory_evaluation,
    evaluate_theory,
    get_theory_score,
    delete_theory_score,
    EvaluateTheoryPOSTRequest,
    TheoryEvaluationScoreRequest,
    TheoryEvaluationDeleteRequest,
)
from theory_evaluation.utils import (
    validate_user,
    get_marking_scheme,
    manage_user_performance,
    get_user_performance,
    delete_user_performance,
)
from theory_evaluation.llm_handler import OpenAI_llm
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings

@pytest.mark.asyncio
async def test_process_theory_evaluation_success(mocker):
    mocker.patch("theory_evaluation.llm_handler.OpenAI_llm.execute", new_callable=AsyncMock, return_value=iter([{"Evaluation": "Good", "Score": 85, "Grade": "B"}]))
    mocker.patch("theory_evaluation.llm_utils.initialise_prompt", return_value="Prompt")
    mocker.patch("theory_evaluation.llm_utils.initialise_settings", return_value={})
    mocker.patch("theory_evaluation.utils.manage_user_performance", return_value=True)

    await process_theory_evaluation(
        email="test@example.com",
        question_id=UUID("12345678-1234-5678-1234-567812345678"),
        answer="Test answer",
        question="Test question",
        marking_scheme="Test scheme",
        model_answer="Test model answer"
    )

    assert True  # If no exception is raised, the test passes

@pytest.mark.asyncio
async def test_process_theory_evaluation_failure(mocker):
    mocker.patch("theory_evaluation.llm_handler.OpenAI_llm.execute", new_callable=AsyncMock, return_value=iter([{"Invalid": "Data"}]))
    mocker.patch("theory_evaluation.llm_utils.initialise_prompt", return_value="Prompt")
    mocker.patch("theory_evaluation.llm_utils.initialise_settings", return_value={})
    mocker.patch("theory_evaluation.utils.manage_user_performance", return_value=False)

    await process_theory_evaluation(
        email="test@example.com",
        question_id=UUID("12345678-1234-5678-1234-567812345678"),
        answer="Test answer",
        question="Test question",
        marking_scheme="Test scheme",
        model_answer="Test model answer"
    )

    assert True  # If no exception is raised, the test passes

def test_evaluate_theory_missing_fields():
    with pytest.raises(HTTPException) as excinfo:
        client = TestClient(evaluate_theory)
        client.post("/api/v1/evaluate-theory", json={})
    assert excinfo.value.status_code == 400

def test_evaluate_theory_user_not_exist(mocker):
    mocker.patch("theory_evaluation.utils.validate_user", return_value=False)
    client = TestClient(evaluate_theory)
    response = client.post("/api/v1/evaluate-theory", json={
        "email": "test@example.com",
        "uuid": "12345678-1234-5678-1234-567812345678",
        "answer": "Test answer"
    })
    assert response.json() == {
        "status": "Not Accepted",
        "message": "User's email does not exist."
    }

def test_get_theory_score_missing_fields():
    with pytest.raises(HTTPException) as excinfo:
        client = TestClient(get_theory_score)
        client.post("/api/v1/get-theory-score", json={})
    assert excinfo.value.status_code == 400

def test_get_theory_score_user_not_exist(mocker):
    mocker.patch("theory_evaluation.utils.validate_user", return_value=False)
    client = TestClient(get_theory_score)
    response = client.post("/api/v1/get-theory-score", json={
        "email": "test@example.com",
        "uuid": "12345678-1234-5678-1234-567812345678"
    })
    assert response.json() == {
        "user_attempts": 0,
        "evaluation": "No evaluation available.",
        "grade": "No grade available."
    }

def test_delete_theory_score_missing_email():
    with pytest.raises(HTTPException) as excinfo:
        client = TestClient(delete_theory_score)
        client.post("/api/v1/delete-theory-score", json={})
    assert excinfo.value.status_code == 400

def test_delete_theory_score_user_not_exist(mocker):
    mocker.patch("theory_evaluation.utils.validate_user", return_value=False)
    with pytest.raises(HTTPException) as excinfo:
        client = TestClient(delete_theory_score)
        client.post("/api/v1/delete-theory-score", json={
            "email": "test@example.com"
        })
    assert excinfo.value.status_code == 404