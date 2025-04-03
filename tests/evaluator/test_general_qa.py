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
from unittest.mock import patch, AsyncMock, MagicMock
from fastapi import HTTPException
from uuid import UUID
from pydantic import EmailStr
from theory_evaluation.evaluator.general_qa import (
    process_theory_evaluation,
    evaluate_theory,
    get_theory_score,
    delete_theory_score,
    EvaluateTheoryPOSTRequest,
    TheoryEvaluationScoreRequest,
    TheoryEvaluationDeleteRequest,
)

@pytest.mark.asyncio
async def test_process_theory_evaluation_success(mocker):
    mocker.patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="prompt")
    mocker.patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value={})
    mock_llm_completion = mocker.patch("theory_evaluation.evaluator.general_qa.llm_completion", new_callable=AsyncMock)
    mock_llm_completion.execute.return_value = AsyncMock(return_value=[{"Evaluation": "Good", "Score": 5, "Grade": "A"}])
    mock_manage_user_performance = mocker.patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True)

    await process_theory_evaluation(
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678123456781234567812345678"),
        answer="Test answer",
        question="Test question",
        marking_scheme="Test scheme",
        model_answer="Test model answer"
    )

    assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_process_theory_evaluation_failure(mocker):
    mocker.patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="prompt")
    mocker.patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value={})
    mock_llm_completion = mocker.patch("theory_evaluation.evaluator.general_qa.llm_completion", new_callable=AsyncMock)
    mock_llm_completion.execute.return_value = AsyncMock(return_value=[{}])
    mock_manage_user_performance = mocker.patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=False)

    await process_theory_evaluation(
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678123456781234567812345678"),
        answer="Test answer",
        question="Test question",
        marking_scheme="Test scheme",
        model_answer="Test model answer"
    )

    assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_evaluate_theory_success(mocker):
    mock_validate_user = mocker.patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True)
    mock_get_marking_scheme = mocker.patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "scheme", "answer"))
    mock_manage_user_performance = mocker.patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True)
    mock_background_tasks = MagicMock()

    response = EvaluateTheoryPOSTRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678"),
        answer="Test answer"
    )

    result = await evaluate_theory(mock_background_tasks, response)

    assert result == {"status": "Accepted", "message": "Processing started"}

@pytest.mark.asyncio
async def test_evaluate_theory_user_not_exist(mocker):
    mocker.patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=False)
    mock_get_marking_scheme = mocker.patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "scheme", "answer"))
    mock_background_tasks = MagicMock()

    response = EvaluateTheoryPOSTRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678"),
        answer="Test answer"
    )

    result = await evaluate_theory(mock_background_tasks, response)

    assert result == {"status": "Not Accepted", "message": "User's email does not exist."}

@pytest.mark.asyncio
async def test_get_theory_score_success(mocker):
    mock_validate_user = mocker.patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True)
    mock_get_marking_scheme = mocker.patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "scheme", "answer"))
    mock_get_user_performance = mocker.patch("theory_evaluation.evaluator.general_qa.get_user_performance", return_value=(1, "Evaluation", "Grade", 0))

    response = TheoryEvaluationScoreRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678")
    )

    result = await get_theory_score(response)

    assert result == {
        "user_attempts": 1,
        "evaluation": "Evaluation",
        "grade": "Grade"
    }

def test_delete_theory_score_success(mocker):
    mock_validate_user = mocker.patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True)
    mock_delete_user_performance = mocker.patch("theory_evaluation.evaluator.general_qa.delete_user_performance", return_value=True)

    response = TheoryEvaluationDeleteRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678")
    )

    delete_theory_score(response)

    assert mock_delete_user_performance.called

def test_delete_theory_score_user_not_exist(mocker):
    mock_validate_user = mocker.patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=False)

    response = TheoryEvaluationDeleteRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678")
    )

    with pytest.raises(HTTPException) as excinfo:
        delete_theory_score(response)

    assert excinfo.value.status_code == 404