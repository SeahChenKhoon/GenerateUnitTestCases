import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

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
def mock_os_environ():
    with patch.dict(os.environ, {
        "AZURE_OPENAI_ENDPOINT_SWEDEN": "mock_endpoint",
        "AZURE_OPENAI_API_KEY_SWEDEN": "mock_api_key",
        "AZURE_OPENAI_API_VERSION": "mock_api_version",
        "OPENAI_API_KEY": "mock_openai_api_key",
        "AZURE_OPENAI_DEPLOYMENT_NAME": "mock_deployment_name",
        "OPENAI_DEPLOYMENT_NAME": "mock_openai_deployment_name"
    }):
        yield
from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.asyncio
async def test_execute_vision():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="Image response"))])
        # Add the rest of your test logic here
