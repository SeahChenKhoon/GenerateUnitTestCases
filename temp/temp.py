import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch
from theory_evaluation.llm_handler import OpenAI_llm
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm


@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Vision response"
