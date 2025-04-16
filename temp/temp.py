import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


# New Test Case
from unittest.mock import patch, AsyncMock
import pytest
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response1", "response2"]
        
        llm = OpenAI_llm(
            message="Test message",
            mode="vision",
            image_input="test_image_data",
            output="stream"
        )
        
        responses = []
        async for response in llm.execute():
            responses.append(response)
        
        assert responses == ["response1", "response2"]
