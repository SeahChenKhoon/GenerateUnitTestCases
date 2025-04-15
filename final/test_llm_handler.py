
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
@patch('llm_handler.OpenAI_llm.client')
async def test_openai_llm_openai_json_completion(mock_openai):
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "The answer to everything."})
    mock_openai.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(message="Test message", output="json")
    result = await llm._OpenAI_JSON_Completion(messages=[{"role": "system", "content": llm.message}], model=llm.model_name, **llm.config)
    
    assert result == {"answer": "42", "explanation": "The answer to everything."}


import pytest
from unittest.mock import AsyncMock, patch
from unittest.mock import AsyncMock, patch
import pytest

@pytest.mark.asyncio
@patch('openai.OpenAI')
async def test_openai_llm_openai_streaming(mock_openai):
    mock_chunk = AsyncMock()
    mock_chunk.choices[0].delta.content = "streamed content"
    mock_openai.return_value.chat.completions.create.return_value = [mock_chunk]

    llm = OpenAI_llm(message="Test message", output="stream")
    responses = []
    async for response in llm.execute():
        responses.append(response)

    assert responses == ["streamed content"]


from unittest.mock import AsyncMock, patch
import pytest
import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture
def mock_openai():
    with patch('openai.OpenAI') as mock:
        yield mock

@pytest.mark.asyncio
async def test_openai_llm_openai_chat_completion(mock_openai):
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "chat content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(message="Test message")
    response = await llm._OpenAI_Chat_Completion()
    assert response == "chat content"


from unittest.mock import AsyncMock, patch
import pytest
from unittest.mock import AsyncMock, patch

@patch('openai.OpenAI')
async def test_openai_llm_execute_text_generation(mock_openai):
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "generated text"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(message="Test message", useAzureOpenAI=False)
    async for response in llm.execute():
        assert response == "generated text"



import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture
def mock_openai():
    with patch('openai.OpenAI') as mock:
        yield mock

@pytest.mark.asyncio
async def test_openai_llm_execute_vision(mock_openai):
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "vision text"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(
        message="Test message",
        useAzureOpenAI=False,
        mode="vision",
        image_input="base64encodedimage",
        output=None
    )

    responses = []
    async for response in llm.execute():
        responses.append(response)

    assert responses[0] == "vision text"

