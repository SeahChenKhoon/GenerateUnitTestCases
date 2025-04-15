import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_azure_openai

@pytest.mark.asyncio
async def test_execute_vision(mock_openai):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="vision content"))]
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai.return_value = mock_client
