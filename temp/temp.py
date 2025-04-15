import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm

import pytest
from unittest.mock import AsyncMock
@pytest.fixture
def mock_openai_llm():
    with patch('theory_evaluation.llm_handler.OpenAI_llm') as mock_llm:
        yield mock_llm

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "Vision response"
