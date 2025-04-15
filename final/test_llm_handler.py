import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm

import pytest
from unittest.mock import AsyncMock
@pytest.fixture
def mock_openai_llm():
    with patch('theory_evaluation.llm_handler.OpenAI_llm') as mock_llm:
        yield mock_llm

from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('os.getenv', side_effect=lambda key: f"mock_{key}"):
        
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.client == mock_azure_openai.return_value
        assert llm.azure_endpoint == "mock_AZURE_OPENAI_ENDPOINT_SWEDEN"
        assert llm.api_version == "mock_AZURE_OPENAI_API_VERSION"
        
        llm = OpenAI_llm(useAzureOpenAI=False)
        assert llm.client == mock_openai.return_value

from unittest.mock import AsyncMock
import json
import pytest

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "The answer to life."})
    # Add your test logic here using mock_response

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = AsyncMock()
    mock_chunk.choices[0].delta.content = "streaming content"

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "Chat completion content"

@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "Generated text"

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "Vision response"
