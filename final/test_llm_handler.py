import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest


@pytest.mark.asyncio
async def test_openai_llm_init():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.os.getenv', side_effect=lambda key: f"{key}_value"):
        
        llm = OpenAI_llm(useAzureOpenAI=True, message="Test message", output="json", mode="text_generation")
        assert llm.message == "Test message"
        assert llm.output == "json"
        assert llm.mode == "text_generation"
        assert llm.client == mock_azure_openai.return_value

@pytest.mark.asyncio
async def test_openai_json_completion():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client') as mock_client:
        mock_response = AsyncMock()
        mock_response.choices[0].message.content = '{"answer": "Test answer", "explanation": "Test explanation"}'
        mock_client.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_openai_streaming():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client') as mock_client:
        mock_stream = AsyncMock()
        mock_chunk = AsyncMock()
        mock_chunk.choices[0].delta.content = "Test content"
        mock_stream.__aiter__.return_value = [mock_chunk]
        mock_client.chat.completions.create.return_value = mock_stream

@pytest.mark.asyncio
async def test_openai_chat_completion():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client') as mock_client:
        mock_response = AsyncMock()
        mock_response.choices[0].message.content = "Test content"
        mock_client.chat.completions.create.return_value = mock_response

@pytest.mark.asyncio
async def test_run_json_output():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._OpenAI_JSON_Completion', return_value={"answer": "Test answer"}) as mock_json_completion:
        llm = OpenAI_llm(message="Test message", output="json")
        result = [content async for content in llm._run()]
        assert result == [{"answer": "Test answer"}]
        assert mock_json_completion.called

@pytest.mark.asyncio
async def test_run_stream_output():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._OpenAI_Streaming', return_value=AsyncMock(__aiter__=lambda s: iter(["Test stream"]))) as mock_streaming:
        llm = OpenAI_llm(message="Test message", output="stream")
        result = [content async for content in llm._run()]
        assert result == ["Test stream"]
        assert mock_streaming.called

@pytest.mark.asyncio
async def test_run_default_output():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._OpenAI_Chat_Completion', return_value="Test chat") as mock_chat_completion:
        llm = OpenAI_llm(message="Test message", output=None)
        result = [content async for content in llm._run()]
        assert result == ["Test chat"]
        assert mock_chat_completion.called

@pytest.mark.asyncio
async def test_execute_text_generation_mode():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', return_value=AsyncMock(__aiter__=lambda s: iter(["Test response"]))) as mock_run:
        llm = OpenAI_llm(message="Test message", mode="text_generation")
        result = [response async for response in llm.execute()]
        assert result == ["Test response"]
        assert mock_run.called

@pytest.mark.asyncio
async def test_execute_vision_mode():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', return_value=AsyncMock(__aiter__=lambda s: iter(["Test response"]))) as mock_run:
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="image_data")
        result = [response async for response in llm.execute()]
        assert result == ["Test response"]
        assert mock_run.called
