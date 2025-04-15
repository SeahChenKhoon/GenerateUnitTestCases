import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
import pytest
from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", return_value="test_value"):
        
        llm = OpenAI_llm(useAzureOpenAI=True, message="Test message", output="json")
        assert llm.message == "Test message"
        assert llm.output == "json"
        assert llm.client == mock_azure_openai.return_value

from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm
import pytest

@pytest.mark.asyncio
async def test_openai_streaming():
    with patch.object(OpenAI_llm, 'client', create=True) as mock_client:
        mock_stream = [MagicMock(), MagicMock()]
        mock_stream[0].choices[0].delta.content = "Hello"
        mock_stream[1].choices[0].delta.content = "World"
        mock_client.chat.completions.create.return_value = mock_stream

@pytest.mark.asyncio
async def test_execute_text_generation():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run") as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response1", "response2"]

@pytest.mark.asyncio
async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run") as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response1", "response2"]
