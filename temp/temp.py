import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock

@pytest.fixture
def mock_os_environ():
    with patch.dict(os.environ, {
        'AZURE_OPENAI_ENDPOINT_SWEDEN': 'mock_endpoint',
        'AZURE_OPENAI_API_VERSION': 'mock_version',
        'AZURE_OPENAI_API_KEY_SWEDEN': 'mock_key',
        'OPENAI_API_KEY': 'mock_openai_key',
        'AZURE_OPENAI_DEPLOYMENT_NAME': 'mock_deployment_name',
        'OPENAI_DEPLOYMENT_NAME': 'mock_openai_deployment_name'
    }):
        yield

# New Test Case
from unittest.mock import patch, MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_execute_vision(mock_openai):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = 'response_content'
    mock_openai.return_value.chat.completions.create = AsyncMock(return_value=mock_response)
