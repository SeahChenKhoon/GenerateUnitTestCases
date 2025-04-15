
from unittest.mock import patch
import asyncio
import json
import os
from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest

from unittest.mock import MagicMock, patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision response"
    with patch.object(OpenAI_llm, "client", create=True) as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="mock_image")
        async for response in llm.execute():
            assert response == "vision response"
