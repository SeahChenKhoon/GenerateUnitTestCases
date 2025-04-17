import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest

@pytest.fixture
def mock_openai_client():
    with patch('llm_handler.OpenAI') as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai_client():
    with patch('llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_azure_openai

import pytest
from unittest.mock import MagicMock, patch
from llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_OpenAI_Streaming_yields_content(mock_openai_client):
    mock_stream = MagicMock()
    mock_stream.__iter__.return_value = iter([MagicMock(choices=[MagicMock(delta=MagicMock(content="chunk1"))]), MagicMock(choices=[MagicMock(delta=MagicMock(content="chunk2"))])])
    mock_openai_client.return_value.chat.completions.create.return_value = mock_stream
    llm = OpenAI_llm(useAzureOpenAI=False)
    chunks = [chunk async for chunk in llm._OpenAI_Streaming()]
    assert chunks == ["chunk1", "chunk2"]

@pytest.fixture
def mock_openai_client():
    with patch('llm_handler.OpenAI') as mock_openai:
        yield mock_openai
