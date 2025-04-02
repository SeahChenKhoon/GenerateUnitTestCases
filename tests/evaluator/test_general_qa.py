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

```python
import pytest
from unittest.mock import AsyncMock, patch
from uuid import UUID
from fastapi import HTTPException, BackgroundTasks
from theory_evaluation.evaluator.general_qa import (
    process_theory_evaluation,
    evaluate_theory,
    get_theory_score,
    delete_theory_score,
    EvaluateTheoryPOSTRequest,
    TheoryEvaluationScoreRequest,
    TheoryEvaluationDeleteRequest
)

@pytest.mark.asyncio
async def test_process_theory_evaluation_successful():
    with patch("theory_evaluation.evaluator.general_qa.manage_user_performance", AsyncMock(return_value=True)) as mock_manage, \
         patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="prompt"), \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value="settings"), \
         patch("theory_evaluation.evaluator.general_qa.llm_completion.execute", AsyncMock(return_value=iter([{"Evaluation": "Good", "Score": 90, "Grade": "A"}]))):
        await process_theory_evaluation("test@example.com", UUID("12345678-1234-5678-1234-567812345678"), "answer", "question", "marking_scheme", "model_answer")
        mock_manage.assert_called()

@pytest.mark.asyncio
async def test_process_theory_evaluation_failure():
    with patch("theory_evaluation.evaluator.general_qa.manage_user_performance", AsyncMock(return_value=False)), \
         patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="prompt"), \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value="settings"), \
         patch("theory_evaluation.evaluator.general_qa.llm_completion.execute", AsyncMock(return_value=iter([{"Evaluation": None, "Score": None, "Grade": None}]))):
        await process_theory_evaluation("test@example.com", UUID("12345678-1234-5678-1234-567812345678"), "answer", "question", "marking_scheme", "model_answer")

@pytest.mark.asyncio
async def test_evaluate_theory_successful():
    request = EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"), answer="answer")
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True), \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "marking_scheme", "model_answer")), \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance", AsyncMock(return_value=True)), \
         patch("theory_evaluation.evaluator.general_qa.BackgroundTasks.add_task", AsyncMock()) as mock_add_task:
        response = await evaluate_theory(BackgroundTasks(), request)
        assert response == {"status": "Accepted", "message": "Processing started"}
        mock_add_task.assert_called()

@pytest.mark.asyncio
async def test_get_theory_score_successful():
    request = TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True), \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "marking_scheme", "model_answer")), \
         patch("theory_evaluation.evaluator.general_qa.get_user_performance", return_value=(3, "Good", "A", 2)):
        response = await get_theory_score(request)
        assert response == {
            "user_attempts": 3,
            "evaluation": "Good\n\nModel Answer: model_answer",
            "grade": "A",
        }

@pytest.mark.asyncio
async def test_delete_theory_score_successful():
    request = TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True), \
         patch("theory_evaluation.evaluator.general_qa.delete_user_performance", return_value=True):
        response = delete_theory_score(request)
        assert response is None

@pytest.mark.asyncio
async def test_delete_theory_score_failure():
    request = TheoryEvaluationDeleteRequest(email="test@example.com")
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=False):
        with pytest.raises(HTTPException) as exc_info:
            delete_theory_score(request)
        assert exc_info.value.status_code == 404
```