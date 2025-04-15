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

@pytest.mark.asyncio
async def test_execute_vision(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "vision response"
    mock_openai.return_value.chat.completions.create.return_value = mock_response
