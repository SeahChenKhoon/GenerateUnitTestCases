import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


# New Test Case
from unittest.mock import MagicMock, patch, PropertyMock
import pytest
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_execute_streaming():
    mock_client = MagicMock()
    type(mock_client).chat = PropertyMock(return_value=MagicMock())
    mock_client.chat.completions.create.return_value = iter([
        MagicMock(choices=[MagicMock(delta=MagicMock(content="streaming data"))]),
        MagicMock(choices=[MagicMock(delta=MagicMock(content="more streaming data"))]),
    ])
    with patch.object(OpenAI_llm, 'client', new_callable=PropertyMock, return_value=mock_client):
        llm = OpenAI_llm(
            message="Test message",
            useAzureOpenAI=False,
            output="stream",
            mode="text_generation",
            verbose=False,
        )
        responses = []
        async for response in llm.execute():
            responses.append(response)
        assert responses == ["streaming data", "more streaming data"]
