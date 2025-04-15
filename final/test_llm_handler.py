import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

@pytest.fixture
def mock_openai_client():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai_client():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai:
        yield mock_azure_openai
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_openai_client():
    return MagicMock()

@pytest.mark.asyncio
async def test_openai_llm_initialization_with_openai(mock_openai_client):
    llm = OpenAI_llm(message="Test message", useAzureOpenAI=False)
    assert llm.message == "Test message"
    assert isinstance(llm.client, MagicMock)


import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization_with_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai_client:
        llm = OpenAI_llm(message="Test message", useAzureOpenAI=True)
        assert llm.message == "Test message"
        assert isinstance(llm.client, mock_azure_openai_client)


from unittest.mock import patch
import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
@patch('llm_handler.OpenAI_llm.client', new_callable=AsyncMock)
async def test_openai_llm_execute_text_generation(mock_openai_client):
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = "Generated text"
    mock_openai_client.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(message="Test message", useAzureOpenAI=False)
    async for response in llm.execute():
        assert response == "Generated text"


import pytest
from unittest.mock import AsyncMock
import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_openai_llm_execute_json_output():
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = json.dumps({"answer": "42"})

    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_openai.return_value.chat.completions.create.return_value = mock_response
        llm = OpenAI_llm(message="Test message", output="json")
        async for response in llm.execute():
            assert response == {"answer": "42"}


import json
from unittest.mock import patch
import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
@patch('llm_handler.OpenAI_llm.client', new_callable=AsyncMock)
async def test_openai_llm_execute_stream_output(mock_openai_client):
    mock_stream = AsyncMock()
    mock_chunk = AsyncMock()
    mock_chunk.choices = [AsyncMock()]
    mock_chunk.choices[0].delta.content = "streamed text"
    mock_stream.__aiter__.return_value = [mock_chunk]
    mock_openai_client.chat.completions.create.return_value = mock_stream

    llm = OpenAI_llm(message="test", useAzureOpenAI=False, output="stream")
    async for token in llm.execute():
        assert token == "streamed text"

