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
    with patch("theory_evaluation.evaluator.general_qa.initialise_prompt") as mock_initialise_prompt, \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings") as mock_initialise_settings, \
         patch("theory_evaluation.evaluator.general_qa.llm_completion.execute", new_callable=AsyncMock) as mock_execute, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance") as mock_manage_user_performance:
        
        mock_initialise_prompt.return_value = "prompt"
        mock_initialise_settings.return_value = {}
        mock_execute.return_value = [{"Evaluation": "Good", "Score": 90, "Grade": "A"}]
        mock_manage_user_performance.return_value = True

        email = "test@example.com"
        question_id = UUID("12345678123456781234567812345678")
        answer = "Test answer"
        question = "Test question"
        marking_scheme = "Test marking scheme"
        model_answer = "Test model answer"

        await process_theory_evaluation(email, question_id, answer, question, marking_scheme, model_answer)

        assert mock_manage_user_performance.call_count == 1

@pytest.mark.asyncio
async def test_process_theory_evaluation_failure():
    with patch("theory_evaluation.evaluator.general_qa.initialise_prompt") as mock_initialise_prompt, \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings") as mock_initialise_settings, \
         patch("theory_evaluation.evaluator.general_qa.llm_completion.execute", new_callable=AsyncMock) as mock_execute, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance") as mock_manage_user_performance:
        
        mock_initialise_prompt.return_value = "prompt"
        mock_initialise_settings.return_value = {}
        mock_execute.return_value = [{}]
        mock_manage_user_performance.return_value = False

        email = "test@example.com"
        question_id = UUID("12345678123456781234567812345678")
        answer = "Test answer"
        question = "Test question"
        marking_scheme = "Test marking scheme"
        model_answer = "Test model answer"

        await process_theory_evaluation(email, question_id, answer, question, marking_scheme, model_answer)

        assert mock_manage_user_performance.call_count == 1

@pytest.mark.asyncio
async def test_evaluate_theory_success():
    with patch("theory_evaluation.evaluator.general_qa.validate_user") as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme") as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance") as mock_manage_user_performance, \
         patch("theory_evaluation.evaluator.general_qa.BackgroundTasks") as mock_background_tasks:
        
        mock_validate_user.return_value = True
        mock_get_marking_scheme.return_value = ("question", "marking_scheme", "model_answer")
        mock_manage_user_performance.return_value = True

        response = EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"), answer="Test answer")
        result = await evaluate_theory(mock_background_tasks, response)

        assert result["status"] == "Accepted"
        assert result["message"] == "Processing started"

@pytest.mark.asyncio
async def test_evaluate_theory_failure():
    with patch("theory_evaluation.evaluator.general_qa.validate_user") as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme") as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance") as mock_manage_user_performance:
        
        mock_validate_user.return_value = False
        mock_get_marking_scheme.return_value = (None, None, None)
        mock_manage_user_performance.return_value = False

        response = EvaluateTheoryPOSTRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"), answer="Test answer")
        result = await evaluate_theory(AsyncMock(), response)

        assert result["status"] == "Not Accepted"
        assert result["message"] == "User's email does not exist."

@pytest.mark.asyncio
async def test_get_theory_score_success():
    with patch("theory_evaluation.evaluator.general_qa.validate_user") as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme") as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.get_user_performance") as mock_get_user_performance:
        
        mock_validate_user.return_value = True
        mock_get_marking_scheme.return_value = ("question", "marking_scheme", "model_answer")
        mock_get_user_performance.return_value = (3, "Evaluation", "A", 0)

        response = TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"))
        result = await get_theory_score(response)

        assert result["user_attempts"] == 3
        assert result["evaluation"] == "Evaluation\n\nModel Answer: model_answer"
        assert result["grade"] == "A"

@pytest.mark.asyncio
async def test_get_theory_score_failure():
    with patch("theory_evaluation.evaluator.general_qa.validate_user") as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme") as mock_get_marking_scheme:
        
        mock_validate_user.return_value = False
        mock_get_marking_scheme.return_value = (None, None, None)

        response = TheoryEvaluationScoreRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"))
        result = await get_theory_score(response)

        assert result["user_attempts"] == 0
        assert result["evaluation"] == "No evaluation available."
        assert result["grade"] == "No grade available."

def test_delete_theory_score_success():
    with patch("theory_evaluation.evaluator.general_qa.validate_user") as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.delete_user_performance") as mock_delete_user_performance:
        
        mock_validate_user.return_value = True
        mock_delete_user_performance.return_value = True

        response = TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"))
        result = delete_theory_score(response)

        assert result is None

def test_delete_theory_score_failure():
    with patch("theory_evaluation.evaluator.general_qa.validate_user") as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.delete_user_performance") as mock_delete_user_performance:
        
        mock_validate_user.return_value = False
        mock_delete_user_performance.return_value = False

        response = TheoryEvaluationDeleteRequest(email="test@example.com", uuid=UUID("12345678123456781234567812345678"))
        
        with pytest.raises(HTTPException) as excinfo:
            delete_theory_score(response)
        
        assert excinfo.value.status_code == 404