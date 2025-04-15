import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch, MagicMock, AsyncMock
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_azure_openai

from unittest.mock import patch, MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_openai_json_completion():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content=json.dumps({"answer": "42"})))]
        mock_openai.return_value.chat.completions.create = AsyncMock(return_value=mock_response)
        # Add your test logic here

from unittest.mock import patch, MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_openai_streaming():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_chunk = MagicMock()
        mock_chunk.choices = [MagicMock(delta=MagicMock(content="streaming content"))]
        mock_openai.return_value.chat.completions.create = AsyncMock(return_value=[mock_chunk])

@pytest.mark.asyncio
async def test_openai_chat_completion(mock_openai):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="chat content"))]
    mock_openai.return_value.chat.completions.create = AsyncMock(return_value=mock_response)

@pytest.mark.asyncio
async def test_execute_text_generation(mock_openai):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="response content"))]
    mock_openai.return_value.chat.completions.create = AsyncMock(return_value=mock_response)

@pytest.mark.asyncio
async def test_execute_vision(mock_openai):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="vision response"))]
    mock_openai.return_value.chat.completions.create = AsyncMock(return_value=mock_response)
