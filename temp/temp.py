import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytestfrom unittest.mock import patch
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock
import pytest
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
@patch('openai.AzureOpenAI')
@patch('openai.OpenAI')
async def test_execute_vision(mock_openai, mock_azure_openai):
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = "test_content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(
        message="Test message",
        useAzureOpenAI=False,
        mode="vision",
        image_input="test_image_input"
    )

    responses = []
    async for response in llm.execute():
        responses.append(response)

    assert responses == ["test_content"]
