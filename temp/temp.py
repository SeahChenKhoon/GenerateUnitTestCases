import pytest
from theory_evaluation import config
from theory_evaluation.evaluator import general_qa
import fastapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from theory_evaluation.main import health_check, shutdown_event, startup_event
import pytest
from fastapi.testclient import TestClient
from theory_evaluation.main import APP, health_check, shutdown_event, startup_event
import logging

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
