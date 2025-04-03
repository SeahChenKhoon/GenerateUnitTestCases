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
async def test_process_theory_evaluation(mocker):
    mock_initialise_prompt = mocker.patch('theory_evaluation.evaluator.general_qa.initialise_prompt', return_value="prompt")
    mock_initialise_settings = mocker.patch('theory_evaluation.evaluator.general_qa.initialise_settings', return_value={})
    mock_llm_completion = mocker.patch('theory_evaluation.evaluator.general_qa.llm_completion')
    mock_llm_completion.execute = AsyncMock(return_value=[{"Evaluation": "Good", "Score": 90, "Grade": "A"}])
    mock_manage_user_performance = mocker.patch('theory_evaluation.evaluator.general_qa.manage_user_performance', return_value=True)

    await process_theory_evaluation(
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678123456781234567812345678"),
        answer="Test Answer",
        question="Test Question",
        marking_scheme="Test Marking Scheme",
        model_answer="Test Model Answer"
    )

    assert mock_initialise_prompt.called
    assert mock_initialise_settings.called
    assert mock_llm_completion.execute.called
    assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_evaluate_theory(mocker):
    mock_validate_user = mocker.patch('theory_evaluation.evaluator.general_qa.validate_user', return_value=True)
    mock_get_marking_scheme = mocker.patch('theory_evaluation.evaluator.general_qa.get_marking_scheme', return_value=("Question", "Marking Scheme", "Model Answer"))
    mock_manage_user_performance = mocker.patch('theory_evaluation.evaluator.general_qa.manage_user_performance', return_value=True)
    mock_background_tasks = MagicMock()

    request = EvaluateTheoryPOSTRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678"),
        answer="Test Answer"
    )

    response = await evaluate_theory(mock_background_tasks, request)

    assert response == {"status": "Accepted", "message": "Processing started"}
    assert mock_validate_user.called
    assert mock_get_marking_scheme.called
    assert mock_manage_user_performance.called
    assert mock_background_tasks.add_task.called

@pytest.mark.asyncio
async def test_get_theory_score(mocker):
    mock_validate_user = mocker.patch('theory_evaluation.evaluator.general_qa.validate_user', return_value=True)
    mock_get_marking_scheme = mocker.patch('theory_evaluation.evaluator.general_qa.get_marking_scheme', return_value=("Question", "Marking Scheme", "Model Answer"))
    mock_get_user_performance = mocker.patch('theory_evaluation.evaluator.general_qa.get_user_performance', return_value=(1, "Evaluation", "Grade", 0))

    request = TheoryEvaluationScoreRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678")
    )

    response = await get_theory_score(request)

    assert response == {
        "user_attempts": 1,
        "evaluation": "Evaluation",
        "grade": "Grade"
    }
    assert mock_validate_user.called
    assert mock_get_marking_scheme.called
    assert mock_get_user_performance.called

def test_delete_theory_score(mocker):
    mock_validate_user = mocker.patch('theory_evaluation.evaluator.general_qa.validate_user', return_value=True)
    mock_delete_user_performance = mocker.patch('theory_evaluation.evaluator.general_qa.delete_user_performance', return_value=True)

    request = TheoryEvaluationDeleteRequest(
        email="test@example.com",
        uuid=UUID("12345678123456781234567812345678")
    )

    response = delete_theory_score(request)

    assert response is None
    assert mock_validate_user.called
    assert mock_delete_user_performance.called