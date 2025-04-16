import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.os.getenv', side_effect=lambda key: f"{key}_value"):
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.azure_endpoint == "AZURE_OPENAI_ENDPOINT_SWEDEN_value"
        assert llm.api_version == "AZURE_OPENAI_API_VERSION_value"
        assert llm.client == mock_azure_openai.return_value

from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = json.dumps({"answer": "test_answer", "explanation": "test_explanation"})

import pytest_asyncio
import pytest
import asyncio
from unittest.mock import MagicMock
from theory_evaluation.llm_handler import OpenAI_llm

@pytest_asyncio.fixture
async def mock_openai_llm():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content='{"answer": "7", "explanation": "2+5 equals 7."}'))]
    )
    llm = OpenAI_llm(useAzureOpenAI=False)
    llm.client = mock_client
    return llm

@pytest.mark.asyncio
async def test_openai_json_completion(mock_openai_llm):
    response = await mock_openai_llm._OpenAI_JSON_Completion()
    assert response == {"answer": "7", "explanation": "2+5 equals 7."}

@pytest.mark.asyncio
async def test_openai_chat_completion(mock_openai_llm):
    response = await mock_openai_llm._OpenAI_Chat_Completion()
    assert response == '{"answer": "7", "explanation": "2+5 equals 7."}'

@pytest.mark.asyncio
async def test_execute(mock_openai_llm):
    responses = []
    async for response in mock_openai_llm.execute():
        responses.append(response)
    assert responses == ['{"answer": "7", "explanation": "2+5 equals 7."}']

from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "chat_content"

from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "vision_content"
