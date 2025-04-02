import pytest
from . import config
from .evaluator import general_qa
import fastapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from theory_evaluation.main import health_check

```python
import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from theory_evaluation.main import APP, health_check

@pytest.fixture
def client():
    with TestClient(APP) as client:
        yield client

def test_health_check_returns_healthy_status(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@patch("theory_evaluation.main.logger.info")
def test_startup_event_logs_correct_message(mock_logger_info):
    with TestClient(APP) as client:
        pass
    mock_logger_info.assert_called_with("Starting up the FastAPI application")

@patch("theory_evaluation.main.logger.info")
def test_shutdown_event_logs_correct_message(mock_logger_info):
    with TestClient(APP) as client:
        pass
    mock_logger_info.assert_called_with("Shutting down the FastAPI application")
```