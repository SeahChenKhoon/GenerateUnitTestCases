import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest


async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", side_effect=lambda key: f"mock_{key}"):
        
        llm = OpenAI_llm(useAzureOpenAI=True, message="Test message")
        assert llm.message == "Test message"
        assert llm.client == mock_azure_openai.return_value
        assert llm.model_name == "mock_AZURE_OPENAI_DEPLOYMENT_NAME"

async def test_openai_json_completion():
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_response = AsyncMock()
        mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "The answer to life"})
        mock_client.chat.completions.create.return_value = mock_response

async def test_openai_streaming():
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_stream = AsyncMock()
        mock_chunk = AsyncMock()
        mock_chunk.choices[0].delta.content = "streaming content"
        mock_stream.__aiter__.return_value = [mock_chunk]
        mock_client.chat.completions.create.return_value = mock_stream

async def test_openai_chat_completion():
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_response = AsyncMock()
        mock_response.choices[0].message.content = "chat completion content"
        mock_client.chat.completions.create.return_value = mock_response

async def test_execute_text_generation():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]

async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]
