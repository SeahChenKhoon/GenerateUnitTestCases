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
from theory_evaluation.main import APP, health_check, startup_event, shutdown_event

@pytest.fixture
def client():
    with TestClient(APP) as client:
        yield client

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@patch('theory_evaluation.main.logger')
def test_startup_event(mock_logger):
    APP.router.startup()
    mock_logger.info.assert_called_once_with("Starting up the FastAPI application")

@patch('theory_evaluation.main.logger')
def test_shutdown_event(mock_logger):
    APP.router.shutdown()
    mock_logger.info.assert_called_once_with("Shutting down the FastAPI application")
```