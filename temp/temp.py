import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT_SWEDEN", "test_endpoint")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "test_version")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY_SWEDEN", "test_api_key")
    monkeypatch.setenv("OPENAI_API_KEY", "test_openai_key")
    monkeypatch.setenv("AZURE_OPENAI_DEPLOYMENT_NAME", "test_deployment_name")
    monkeypatch.setenv("OPENAI_DEPLOYMENT_NAME", "test_openai_deployment_name")
import pytest

@pytest.fixture
def sample_fixture():
    return "sample data"

def test_sample_fixture(sample_fixture):
    assert sample_fixture == "sample data"
