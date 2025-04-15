import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm


import pytest
from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('os.getenv', side_effect=lambda key: f"mock_{key}"):
        
        llm = OpenAI_llm(useAzureOpenAI=True, message="Test message")
        assert llm.message == "Test message"
        assert llm.client == mock_azure.return_value
        assert hasattr(llm.client, 'chat')

from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "The answer to life."})
    # Add additional test logic here as needed

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "streaming content"

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Chat completion content"

@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Generated text"

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Vision response"
