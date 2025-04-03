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

@pytest.mark.asyncio
async def test_process_theory_evaluation_success():
    with patch("theory_evaluation.evaluator.general_qa.initialise_prompt", return_value="prompt") as mock_initialise_prompt, \
         patch("theory_evaluation.evaluator.general_qa.initialise_settings", return_value={}) as mock_initialise_settings, \
         patch("theory_evaluation.evaluator.general_qa.OpenAI_llm.execute", new_callable=AsyncMock) as mock_execute, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True) as mock_manage_user_performance:
        
        mock_execute.return_value = [{"Evaluation": "Good", "Score": 90, "Grade": "A"}]
        
        await process_theory_evaluation(
            email="test@example.com",
            question_id="12345678-1234-5678-1234-567812345678",
            answer="Test answer",
            question="Test question",
            marking_scheme="Test scheme",
            model_answer="Test model answer"
        )
        
        assert mock_initialise_prompt.called
        assert mock_initialise_settings.called
        assert mock_execute.called
        assert mock_manage_user_performance.called

@pytest.mark.asyncio
async def test_evaluate_theory_success():
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True) as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "scheme", "model")) as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.manage_user_performance", return_value=True) as mock_manage_user_performance, \
         patch("theory_evaluation.evaluator.general_qa.BackgroundTasks.add_task") as mock_add_task:
        
        response = EvaluateTheoryPOSTRequest(
            email="test@example.com",
            uuid="12345678-1234-5678-1234-567812345678",
            answer="Test answer"
        )
        
        background_tasks = AsyncMock()
        
        result = await evaluate_theory(background_tasks, response)
        
        assert result == {"status": "Accepted", "message": "Processing started"}
        assert mock_validate_user.called
        assert mock_get_marking_scheme.called
        assert mock_manage_user_performance.called
        assert mock_add_task.called

@pytest.mark.asyncio
async def test_get_theory_score_success():
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True) as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.get_marking_scheme", return_value=("question", "scheme", "model")) as mock_get_marking_scheme, \
         patch("theory_evaluation.evaluator.general_qa.get_user_performance", return_value=(1, "Evaluation", "Grade", 0)) as mock_get_user_performance:
        
        response = TheoryEvaluationScoreRequest(
            email="test@example.com",
            uuid="12345678-1234-5678-1234-567812345678"
        )
        
        result = await get_theory_score(response)
        
        assert result == {
            "user_attempts": 1,
            "evaluation": "Evaluation",
            "grade": "Grade"
        }
        assert mock_validate_user.called
        assert mock_get_marking_scheme.called
        assert mock_get_user_performance.called

def test_delete_theory_score_success():
    with patch("theory_evaluation.evaluator.general_qa.validate_user", return_value=True) as mock_validate_user, \
         patch("theory_evaluation.evaluator.general_qa.delete_user_performance", return_value=True) as mock_delete_user_performance:
        
        response = TheoryEvaluationDeleteRequest(
            email="test@example.com",
            uuid="12345678-1234-5678-1234-567812345678"
        )
        
        result = delete_theory_score(response)
        
        assert result is None
        assert mock_validate_user.called
        assert mock_delete_user_performance.called

def test_evaluate_theory_missing_fields():
    response = EvaluateTheoryPOSTRequest(
        email="",
        uuid="",
        answer=""
    )
    
    background_tasks = AsyncMock()
    
    with pytest.raises(HTTPException) as excinfo:
        evaluate_theory(background_tasks, response)
    
    assert excinfo.value.status_code == 400

def test_get_theory_score_missing_fields():
    response = TheoryEvaluationScoreRequest(
        email="",
        uuid=""
    )
    
    with pytest.raises(HTTPException) as excinfo:
        get_theory_score(response)
    
    assert excinfo.value.status_code == 400

def test_delete_theory_score_missing_email():
    response = TheoryEvaluationDeleteRequest(
        email=""
    )
    
    with pytest.raises(HTTPException) as excinfo:
        delete_theory_score(response)
    
    assert excinfo.value.status_code == 400
```