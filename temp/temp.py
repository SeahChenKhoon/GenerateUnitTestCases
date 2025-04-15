import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock

@pytest.fixture
def mock_os_environ():
    with patch.dict(os.environ, {
        "AZURE_OPENAI_ENDPOINT_SWEDEN": "https://example.com",
        "AZURE_OPENAI_API_VERSION": "v1",
        "AZURE_OPENAI_API_KEY_SWEDEN": "fake_key",
        "OPENAI_API_KEY": "fake_key",
        "AZURE_OPENAI_DEPLOYMENT_NAME": "azure_model",
        "OPENAI_DEPLOYMENT_NAME": "openai_model"
    }):
        yield
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_execute_vision():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Vision response"
        mock_openai.return_value.chat.completions.create.return_value = mock_response

        llm = OpenAI_llm(
            message="Test message",
            mode="vision",
            image_input="test_image_data",
            model_name="test_model",
            output=None
        )

        async for response in llm.execute():
            assert response == "Vision response"
