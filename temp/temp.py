import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm

from unittest.mock import patch, MagicMock
import pytest
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_openai_chat_completion():
    with patch("openai.OpenAI.chat.completions.create", return_value=MagicMock(choices=[MagicMock(message=MagicMock(content="chat_content"))])):
        llm = OpenAI_llm(message="Test message")
        content = await llm._OpenAI_Chat_Completion()
        assert content == "chat_content"
