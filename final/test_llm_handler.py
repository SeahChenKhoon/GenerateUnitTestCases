import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch, MagicMock
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_azure_openai

from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_openai_streaming():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_chunk = MagicMock()
        mock_chunk.choices[0].delta.content = "streamed content"
        mock_openai.return_value.chat.completions.create.return_value = [mock_chunk]
        # Add assertions or further test logic here

@pytest.mark.asyncio
async def test_openai_chat_completion(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "chat content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_text_generation(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "generated text"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_vision(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision response"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_error_handling(mock_openai):
    mock_openai.return_value.chat.completions.create.side_effect = Exception("Test error")
