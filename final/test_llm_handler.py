import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

@pytest.fixture
def mock_openai_client():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_openai, mock_azure_openai