import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock, AsyncMock


from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.os.getenv', return_value='mock_value'):
        
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.client == mock_azure_openai.return_value

from unittest.mock import MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = '{"key": "value"}'
    mock_client = AsyncMock()
    mock_client.chat.completions.create.return_value = mock_response

from unittest.mock import MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "streamed content"
    mock_client = AsyncMock()
    mock_client.chat.completions.create.return_value = [mock_chunk]

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "chat content"
    mock_client = AsyncMock()
    mock_client.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "generated text"
    mock_client = AsyncMock()
    mock_client.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision content"
    mock_client = AsyncMock()
    mock_client.chat.completions.create.return_value = mock_response
