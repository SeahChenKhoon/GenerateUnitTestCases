import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
from unittest.mock import AsyncMock
@pytest.fixture
def mock_openai_client():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_openai, mock_azure_openai

from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization(mock_openai_client):
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        mock_openai, mock_azure_openai = mock_openai_client

from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_openai_llm_json_completion(mock_openai_client):
    mock_openai, _ = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content=json.dumps({"answer": "42"})))]
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_openai_llm_streaming(mock_openai_client):
    mock_openai, _ = mock_openai_client
    mock_chunk = AsyncMock()
    mock_chunk.choices = [AsyncMock(delta=AsyncMock(content="chunk"))]
    mock_openai.return_value.chat.completions.create.return_value = [mock_chunk]

@pytest.mark.asyncio
async def test_openai_llm_chat_completion(mock_openai_client):
    mock_openai, _ = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content="response"))]
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_openai_llm_execute_text_generation(mock_openai_client):
    mock_openai, _ = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content="response"))]
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_openai_llm_execute_vision(mock_openai_client):
    mock_openai, _ = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content="response"))]
    mock_openai.return_value.chat.completions.create.return_value = mock_response
