import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


# New Test Case
from unittest.mock import patch
import pytest
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run") as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response data"]
        llm = OpenAI_llm(mode="vision", output="stream", image_input="dummy_image_data")
        responses = []
        async for response in llm.execute():
            responses.append(response)
        assert responses == ["response data"]
