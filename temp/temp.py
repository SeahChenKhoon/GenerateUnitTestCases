import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


# New Test Case
from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision execution content"
    llm = OpenAI_llm(message="Test message", mode="vision", output="stream")
    llm.client.chat.completions.create = MagicMock(return_value=mock_response)
    async for response in llm.execute():
        assert response == "vision execution content"
