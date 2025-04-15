import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest

from unittest.mock import patch, AsyncMock
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value = AsyncMock()
        mock_run.return_value.__aiter__.return_value = ["response1", "response2"]
        
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="mock_image_input", output="json")
        responses = [response async for response in llm.execute()]
        
        assert responses == ["response1", "response2"]
