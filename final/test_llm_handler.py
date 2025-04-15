import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI', autospec=True) as mock_azure_openai:
        yield mock_azure_openai

@pytest.fixture
def mock_env_vars():
    with patch.dict(os.environ, {
        "AZURE_OPENAI_ENDPOINT_SWEDEN": "https://example.com",
        "AZURE_OPENAI_API_VERSION": "v1",
        "AZURE_OPENAI_API_KEY_SWEDEN": "fake_key",
        "OPENAI_API_KEY": "fake_key",
        "AZURE_OPENAI_DEPLOYMENT_NAME": "azure_model",
        "OPENAI_DEPLOYMENT_NAME": "openai_model"
    }):
        yield
