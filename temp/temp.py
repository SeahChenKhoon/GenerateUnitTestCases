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

@pytest.mark.asyncio
async def test_execute_error_handling(mock_openai):
    mock_openai.return_value.chat.completions.create.side_effect = Exception("Test error")
