import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

@pytest.fixture
def mock_openai_client():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_openai, mock_azure_openai
import pytest

@pytest.mark.asyncio
async def test_openai_llm_initialization(mock_openai_client):
    mock_openai, mock_azure_openai = mock_openai_client
    llm = OpenAI_llm(message="Test message", useAzureOpenAI=True)
    assert llm.client == mock_azure_openai