
from unittest.mock import patch
import asyncio
import json
import os
from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", return_value="mock_value"):
        llm = OpenAI_llm(useAzureOpenAI=True, message="Test message")
        assert llm.message == "Test message"
        assert llm.client == mock_azure_openai.return_value
