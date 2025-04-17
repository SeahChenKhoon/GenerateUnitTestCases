import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest



@pytest.mark.asyncio
async def test_openai_llm_openai_streaming():
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_stream = MagicMock()
        mock_stream.__aiter__.return_value = [{"choices": [{"delta": {"content": "chunk1"}}]},
                                              {"choices": [{"delta": {"content": "chunk2"}}]}]
        mock_client.chat.completions.create.return_value = mock_stream
