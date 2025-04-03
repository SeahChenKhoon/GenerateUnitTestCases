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
from unittest.mock import AsyncMock, patch
from fastapi import HTTPException
from theory_evaluation.evaluator.general_qa import (
    process_theory_evaluation,
    evaluate_theory,
    get_theory_score,
    delete_theory_score,
    EvaluateTheoryPOSTRequest,
    TheoryEvaluationScoreRequest,
    TheoryEvaluationDeleteRequest,
)
from uuid import UUID
import pydantic

@pytest.mark.asyncio
async def test_process_theory_evaluation_success():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    answer = "Test answer"
    question = "Test question"
    marking_scheme = "Test marking scheme"
    model_answer = "Test model answer"

    with patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="Prompt") as mock_initialise_prompt, \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value="Settings") as mock_initialise_settings, \
         patch("theory_evaluation.evaluator.general_qa.OpenAI_llm.execute", new_callable=AsyncMock) as mock_execute, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True) as mock_manage_user_performance:
        
        mock_execute.return_value = [{"Evaluation": "Good", "Score": 90, "Grade": "A"}]
        
        await process_theory_evaluation(email, question_id, answer, question, marking_scheme, model_answer)
        
        assert mock_initialise_prompt.called
        assert mock_initialise_settings.called
        assert mock_execute.called
        assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_process_theory_evaluation_failure():
    email = "test@example.com"
    question_id = UUID("12345678-1234-5678-1234-567812345678")
    answer = "Test answer"
    question = "Test question"
    marking_scheme = "Test marking scheme"
    model_answer = "Test model answer"

    with patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="Prompt"), \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value="Settings"), \
         patch("theory_evaluation.evaluator.general_qa.OpenAI_llm.execute", new_callable=AsyncMock) as mock_execute, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=False) as mock_manage_user_performance:
        
        mock_execute.return_value = [{"Evaluation": None, "Score": None, "Grade": None}]
        
        await process_theory_evaluation(email, question_id, answer, question, marking_scheme, model_answer)
        
        assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_evaluate_theory_success():
    background_tasks = AsyncMock()
    response = EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"), answer="Test answer")

    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True) as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("Question", "Marking Scheme", "Model Answer")) as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True) as mock_manage_user_performance:
        
        result = await evaluate_theory(background_tasks, response)
        
        assert mock_validate_user.called
        assert mock_get_marking_scheme.called
        assert mock_manage_user_performance.called
        assert result == {"status": "Accepted", "message": "Processing started"}

@pytest.mark.asyncio
async def test_evaluate_theory_failure():
    background_tasks = AsyncMock()
    response = EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"), answer="Test answer")

    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=False) as mock_validate_user:
        
        result = await evaluate_theory(background_tasks, response)
        
        assert mock_validate_user.called
        assert result == {"status": "Not Accepted", "message": "User's email does not exist."}

@pytest.mark.asyncio
async def test_get_theory_score_success():
    response = TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))

    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True) as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("Question", "Marking Scheme", "Model Answer")) as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.get_user_performance", return_value=(1, "Evaluation", "Grade", 0)) as mock_get_user_performance:
        
        result = await get_theory_score(response)
        
        assert mock_validate_user.called
        assert mock_get_marking_scheme.called
        assert mock_get_user_performance.called
        assert result == {"user_attempts": 1, "evaluation": "Evaluation", "grade": "Grade"}

@pytest.mark.asyncio
async def test_get_theory_score_failure():
    response = TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))

    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=False) as mock_validate_user:
        
        result = await get_theory_score(response)
        
        assert mock_validate_user.called
        assert result == {"user_attempts": 0, "evaluation": "No evaluation available.", "grade": "No grade available."}

def test_delete_theory_score_success():
    response = TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))

    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True) as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.delete_user_performance", return_value=True) as mock_delete_user_performance:
        
        result = delete_theory_score(response)
        
        assert mock_validate_user.called
        assert mock_delete_user_performance.called
        assert result is None

def test_delete_theory_score_failure():
    response = TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678-1234-5678-1234-567812345678"))

    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=False) as mock_validate_user:
        
        with pytest.raises(HTTPException) as excinfo:
            delete_theory_score(response)
        
        assert mock_validate_user.called
        assert excinfo.value.status_code == 404