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
    with patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True) as mock_manage:
        with patch("theory_evaluation.evaluator.general_qa.llm_completion.execute", AsyncMock(return_value=iter([{"Evaluation": "Good", "Score": 80, "Grade": "A"}]))):
            with patch("theory_evaluation.evaluator.general_qa.json.loads", return_value={"Evaluation": "Good", "Score": 80, "Grade": "A"}):
                await process_theory_evaluation("test@example.com", UUID("12345678-1234-5678-1234-567812345678"), "answer", "question", "marking_scheme", "model_answer")
                mock_manage.assert_called_with(mode=1, email="test@example.com", question_id=UUID("12345678-1234-5678-1234-567812345678"), llm_evaluation="Good", llm_score=80, user_grade="A")

@pytest.mark.asyncio
async def test_process_theory_evaluation_failure():
    with patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=False):
        with patch("theory_evaluation.evaluator.general_qa.llm_completion.execute", AsyncMock(return_value=iter([{"Evaluation": "Poor", "Score": 50, "Grade": "F"}]))):
            with patch("theory_evaluation.evaluator.general_qa.json.loads", return_value={"Evaluation": "Poor", "Score": 50, "Grade": "F"}):
                with pytest.raises(Exception):
                    await process_theory_evaluation("test@example.com", UUID("12345678-1234-5678-1234-567812345678"), "answer", "question", "marking_scheme", "model_answer")

@pytest.mark.asyncio
async def test_evaluate_theory_successful():
    request = EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"), answer="answer")
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True):
        with patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "marking_scheme", "model_answer")):
            with patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True):
                with patch("theory_evaluation.evaluator.general_qa.process_theory_evaluation", AsyncMock()):
                    response = await evaluate_theory(BackgroundTasks(), request)
                    assert response == {"status": "Accepted", "message": "Processing started"}

@pytest.mark.asyncio
async def test_get_theory_score_successful():
    request = TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True):
        with patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "marking_scheme", "model_answer")):
            with patch("theory_evaluation.evaluator.general_qa.get_user_performance", return_value=(3, "Good", "A", 2)):
                response = await get_theory_score(request)
                assert response == {"user_attempts": 3, "evaluation": "Good\n\nModel Answer: model_answer", "grade": "A"}

@pytest.mark.asyncio
async def test_delete_theory_score_successful():
    request = TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True):
        with patch("theory_evaluation.evaluator.general_qa.delete_user_performance", return_value=True):
            response = delete_theory_score(request)
            assert response is None
```