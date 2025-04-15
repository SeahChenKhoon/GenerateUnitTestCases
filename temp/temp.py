import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest


@pytest.mark.asyncio
async def test_execute_vision_mode():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', return_value=AsyncMock(__aiter__=lambda s: iter(["Test response"]))) as mock_run:
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="image_data")
        result = [response async for response in llm.execute()]
        assert result == ["Test response"]
        assert mock_run.called
