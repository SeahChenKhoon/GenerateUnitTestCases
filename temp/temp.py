import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock

@pytest.fixture
def mock_os_environ():
    with patch.dict(os.environ, {
        "AZURE_OPENAI_ENDPOINT_SWEDEN": "test_endpoint",
        "AZURE_OPENAI_API_VERSION": "test_version",
        "AZURE_OPENAI_API_KEY_SWEDEN": "test_key",
        "OPENAI_API_KEY": "test_openai_key",
        "AZURE_OPENAI_DEPLOYMENT_NAME": "test_deployment",
        "OPENAI_DEPLOYMENT_NAME": "test_openai_deployment"
    }):
        yield

from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_openai_llm_initialization_with_azure(mock_azure_openai, mock_os_environ):
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.client is mock_azure_openai.return_value
        assert llm.azure_endpoint == "test_endpoint"
        assert llm.api_version == "test_version"
        assert llm.model_name == "test_deployment"

@pytest.mark.asyncio
async def test_openai_llm_initialization_without_azure(mock_openai, mock_os_environ):
    llm = OpenAI_llm(useAzureOpenAI=False)
    assert llm.client is mock_openai.return_value
    assert llm.model_name == "test_openai_deployment"

@pytest.mark.asyncio
async def test_openai_json_completion(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({"key": "value"})
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_openai_streaming(mock_openai):
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "chunk_content"
    mock_openai.return_value.chat.completions.create.return_value = [mock_chunk]

@pytest.mark.asyncio
async def test_openai_chat_completion(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "chat_content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_text_generation(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "response_content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_vision(mock_openai):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "response_content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response
