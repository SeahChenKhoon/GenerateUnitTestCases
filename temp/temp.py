import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


# New Test Case
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"type": "json_object", "content": "vision content"}'
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="image_data", output="json")
        result = [response async for response in llm.execute()]
        assert result == [{"type": "json_object", "content": "vision content"}]
