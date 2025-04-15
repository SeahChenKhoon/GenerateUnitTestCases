import asyncio
import json
import os
import pytest
from unittest.mock import patch, AsyncMock
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock

@pytest.mark.asyncio
async def test_openai_llm_initialization_with_openai(mock_openai):
    os.environ['OPENAI_API_KEY'] = 'test_key'
    llm = OpenAI_llm()
    assert llm.client is mock_openai.return_value
    assert llm.client.api_key == 'test_key'