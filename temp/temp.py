import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
No `@pytest.fixture` functions are present in the provided code.

# New Test Case
from theory_evaluation.llm_handler import OpenAI_llm
import pytest

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision content"
    
    with patch('openai.AzureOpenAI.chat.completions.create', return_value=mock_response):
        llm = OpenAI_llm(
            message="Test message",
            useAzureOpenAI=True,
            mode="vision",
            image_input="base64encodedimage",
            output=None
        )
        
        async for response in llm.execute():
            assert response == "vision content"
