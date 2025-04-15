import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI


import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI


import pytest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", return_value="test_value"):
        
        llm = OpenAI_llm(useAzureOpenAI=True, message="Test message")
        assert llm.message == "Test message"
        assert llm.azure_endpoint == "test_value"
        assert llm.api_version == "test_value"
        assert llm.model_name == "test_value"
        assert hasattr(llm, "client")
        assert mock_azure_openai.called


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "The answer to life"})
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client.chat.completions.create", return_value=mock_response):
        llm = OpenAI_llm(message="Test message")
        result = await llm._OpenAI_JSON_Completion()
        assert result == {"answer": "42", "explanation": "The answer to life"}


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "streaming content"
    mock_stream = AsyncMock(return_value=[mock_chunk])
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client.chat.completions.create", return_value=mock_stream):
        llm = OpenAI_llm(message="Test message", output="stream")
        async for data in llm._OpenAI_Streaming():
            assert data == "streaming content"


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "chat completion content"
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client.chat.completions.create", return_value=mock_response):
        llm = OpenAI_llm(message="Test message")
        result = await llm._OpenAI_Chat_Completion()
        assert result == "chat completion content"


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "execution content"
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client.chat.completions.create", return_value=mock_response):
        llm = OpenAI_llm(message="Test message", output=None)
        async for response in llm.execute():
            assert response == "execution content"


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision content"
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client.chat.completions.create", return_value=mock_response):
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="image_data")
        async for response in llm.execute():
            assert response == "vision content"

