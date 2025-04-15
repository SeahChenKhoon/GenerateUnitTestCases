import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
from unittest.mock import patch, MagicMock


import pytest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", side_effect=lambda key: f"mock_{key}"):
        
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.client == mock_azure_openai.return_value
        assert llm.azure_endpoint == "mock_AZURE_OPENAI_ENDPOINT_SWEDEN"
        assert llm.api_version == "mock_AZURE_OPENAI_API_VERSION"
        assert llm.model_name == "mock_AZURE_OPENAI_DEPLOYMENT_NAME"

from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({"key": "value"})

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "streamed content"

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "chat content"

@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "response content"

@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "response content"
