import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock
from unittest.mock import patch

@pytest.mark.asyncio
@patch('theory_evaluation.llm_handler.OpenAI')
async def test_openai_llm_initialization_with_openai(mock_openai):
    os.environ['OPENAI_API_KEY'] = 'test_key'
    llm = OpenAI_llm()
    assert llm.client is mock_openai.return_value
    assert hasattr(llm.client, 'chat')

