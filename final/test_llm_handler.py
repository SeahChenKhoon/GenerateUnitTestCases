
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
import asyncio
from unittest.mock import MagicMock, patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = '{"answer": "42", "explanation": "The answer to life."}'
    
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        llm = OpenAI_llm(message="Test message")
        result = await llm._OpenAI_JSON_Completion()
        assert result == {"answer": "42", "explanation": "The answer to life."}


import pytest
from unittest.mock import MagicMock, patch
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
import asyncio
from unittest.mock import MagicMock, patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "streaming content"
    
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        mock_client.chat.completions.create.return_value = [mock_chunk]
        llm = OpenAI_llm(message="Test message", output="stream")
        async for content in llm._OpenAI_Streaming():
            assert content == "streaming content"


import asyncio
import pytest
from unittest.mock import MagicMock, patch
import asyncio

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Chat completion content"
    
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        llm = OpenAI_llm(message="Test message")
        result = await llm._OpenAI_Chat_Completion()
        assert result == "Chat completion content"


import pytest
from unittest.mock import MagicMock, patch
import pytest
import asyncio
from unittest.mock import MagicMock, patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Generated text"
    
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        llm = OpenAI_llm(message="Test message", mode="text_generation")
        async for content in llm.execute():
            assert content == "Generated text"


import asyncio
from theory_evaluation.llm_handler import OpenAI_llm
from unittest.mock import MagicMock, patch
import pytest
import asyncio

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Vision response"
    
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="mock_image")
        responses = []
        async for content in llm.execute():
            responses.append(content)
        assert responses == ["Vision response"]

