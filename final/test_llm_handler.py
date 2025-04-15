import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from theory_evaluation.llm_handler import OpenAI_llm
from unittest.mock import patch
from unittest.mock import AsyncMock


from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", side_effect=lambda key: f"mock_{key}"):
        
        llm = OpenAI_llm(
            useAzureOpenAI=True,
            message="Test message",
            output="json",
            mode="text_generation",
            verbose=True
        )
        
        assert llm.message == "Test message"
        assert llm.output == "json"
        assert llm.mode == "text_generation"
        assert llm.verbose is True
        assert hasattr(llm, "client")
        assert mock_azure_openai.called

from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_execute_text_generation():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]

@pytest.mark.asyncio
async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]
