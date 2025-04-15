import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from theory_evaluation.llm_handler import OpenAI_llm
from unittest.mock import patch
from unittest.mock import AsyncMock


@pytest.mark.asyncio
async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run", new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]
