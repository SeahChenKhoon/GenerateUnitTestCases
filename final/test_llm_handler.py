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
import os
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_openai_llm_initialization_with_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        os.environ['OPENAI_API_KEY'] = 'test_key'
        llm = OpenAI_llm(useAzureOpenAI=False)
        assert llm.client == mock_openai.return_value
        assert llm.client.api_key == 'test_key'

