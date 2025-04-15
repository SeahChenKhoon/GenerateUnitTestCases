import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import json
import pytest

from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_execute_vision():
    with patch.object(OpenAI_llm, '_run', return_value=AsyncMock(return_value=["response"])), \
         patch.object(OpenAI_llm, '__init__', return_value=None):
        llm = OpenAI_llm()
        llm.mode = "vision"
        llm.message = "Test message"
        llm.image_input = "image_data"
        responses = [response async for response in llm.execute()]
        assert responses == ["response"]