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
from theory_evaluation.general_qa import delete_theory_score

```python
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from uuid import UUID
from fastapi import HTTPException
from theory_evaluation.general_qa import (
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
    mock_initialise_prompt = mocker.patch("theory_evaluation.general_qa.initialise_prompt", return_value="prompt")
    mock_initialise_settings = mocker.patch("theory_evaluation.general_qa.initialise_settings", return_value={})
    mock_llm_completion = mocker.patch("theory_evaluation.general_qa.llm_completion")
    mock_llm_completion.execute = AsyncMock(return_value=[{"Evaluation": "Good", "Score": 90, "Grade": "A"}])
    mock_manage_user_performance = mocker.patch("theory_evaluation.general_qa.manage_user_performance", return_value=True)

    await process_theory_evaluation(
        email="test@example.com",
        question_id=UUID("12345678123456781234567812345678"),
        answer="Test answer",
        question="Test question",
        marking_scheme="Test marking scheme",
        model_answer="Test model answer",
    )

    assert mock_initialise_prompt.called
    assert mock_initialise_settings.called
    assert mock_llm_completion.execute.called
    assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_evaluate_theory_missing_fields():
    with pytest.raises(HTTPException) as excinfo:
        await evaluate_theory(
            background_tasks=MagicMock(),
            response=EvaluateTheoryPOSTRequest(email="", uuid=UUID("12345678123456781234567812345678"), answer="")
        )
    assert excinfo.value.status_code == 400

@pytest.mark.asyncio
async def test_evaluate_theory_user_not_exist(mocker):
    mocker.patch("theory_evaluation.general_qa.validate_user", return_value=False)
    mocker.patch("theory_evaluation.general_qa.get_marking_scheme", return_value=(None, None, None))

    response = await evaluate_theory(
        background_tasks=MagicMock(),
        response=EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"), answer="Test answer")
    )
    assert response["status"] == "Not Accepted"
    assert response["message"] == "User's email does not exist."

@pytest.mark.asyncio
async def test_get_theory_score_missing_fields():
    with pytest.raises(HTTPException) as excinfo:
        await get_theory_score(
            response=TheoryEvaluationScoreRequest(email="", uuid=UUID("12345678123456781234567812345678"))
        )
    assert excinfo.value.status_code == 400

@pytest.mark.asyncio
async def test_get_theory_score_user_not_exist(mocker):
    mocker.patch("theory_evaluation.general_qa.validate_user", return_value=False)
    mocker.patch("theory_evaluation.general_qa.get_marking_scheme", return_value=(None, None, None))

    response = await get_theory_score(
        response=TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"))
    )
    assert response["user_attempts"] == 0
    assert response["evaluation"] == "No evaluation available."
    assert response["grade"] == "No grade available."

def test_delete_theory_score_missing_email():
    with pytest.raises(HTTPException) as excinfo:
        delete_theory_score(
            response=TheoryEvaluationDeleteRequest(email="", uuid=UUID("12345678123456781234567812345678"))
        )
    assert excinfo.value.status_code == 400

def test_delete_theory_score_user_not_exist(mocker):
    mocker.patch("theory_evaluation.general_qa.validate_user", return_value=False)

    with pytest.raises(HTTPException) as excinfo:
        delete_theory_score(
            response=TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"))
        )
    assert excinfo.value.status_code == 404
```