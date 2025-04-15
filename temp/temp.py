import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
import pytest
from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


@pytest.mark.asyncio
async def test_execute_vision():
    with patch("theory_evaluation.llm_handler.OpenAI_llm._run") as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response1", "response2"]
