import pytest
from theory_evaluation import config
from theory_evaluation.evaluator import general_qa
import fastapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from theory_evaluation.main import health_check, shutdown_event, startup_event
from fastapi.testclient import TestClient
from unittest.mock import patch
from theory_evaluation.main import APP, health_check, shutdown_event, startup_event

@pytest.mark.asyncio
async def test_shutdown_event():
    with patch('theory_evaluation.main.logger') as mock_logger:
        await shutdown_event()
        assert mock_logger.info.called
        assert mock_logger.info.call_args_list[0][0][0] == "Shutting down the FastAPI application"