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

@pytest.mark.asyncio
async def test_openai_llm_execute_vision(mock_openai_client):
    mock_openai, _ = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content="response"))]
    mock_openai.return_value.chat.completions.create.return_value = mock_response
