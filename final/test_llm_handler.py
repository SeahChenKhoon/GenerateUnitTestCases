import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
@pytest.fixture
def mock_openai_client():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        yield mock_azure, mock_openai

import os
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_openai_llm_initialization(mock_openai_client):
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_azure, mock_openai = mock_openai_client
        os.environ['AZURE_OPENAI_ENDPOINT_SWEDEN'] = 'test_endpoint'
        os.environ['AZURE_OPENAI_API_KEY_SWEDEN'] = 'test_key'
        os.environ['AZURE_OPENAI_API_VERSION'] = 'test_version'
        os.environ['AZURE_OPENAI_DEPLOYMENT_NAME'] = 'test_deployment'
        os.environ['OPENAI_API_KEY'] = 'test_openai_key'
        os.environ['OPENAI_DEPLOYMENT_NAME'] = 'test_openai_deployment'

import pytest
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_openai_json_completion(mock_openai_client):
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure:
        _, mock_openai = mock_openai_client
        mock_response = AsyncMock()
        mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "It's the answer."})
        mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_openai_streaming(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_chunk = AsyncMock()
    mock_chunk.choices[0].delta.content = "streamed content"
    mock_openai.return_value.chat.completions.create.return_value = [mock_chunk]

@pytest.mark.asyncio
async def test_openai_chat_completion(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "chat content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_text_generation(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "generated text"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_vision(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "vision response"
    mock_openai.return_value.chat.completions.create.return_value = mock_response
