import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import json
import pytest


from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('os.getenv', side_effect=lambda key: f"{key}_value"):
        # Add your test logic here
        pass

from unittest.mock import MagicMock
import json
import pytest

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = json.dumps({"key": "value"})

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices = [MagicMock()]
    mock_chunk.choices[0].delta.content = "streamed content"

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "chat completion content"
