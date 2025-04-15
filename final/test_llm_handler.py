import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        yield mock_openai

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI', autospec=True) as mock_azure_openai:
        yield mock_azure_openai

@pytest.fixture
def mock_os_environ():
    with patch.dict(os.environ, {
        "AZURE_OPENAI_ENDPOINT_SWEDEN": "mock_endpoint",
        "AZURE_OPENAI_API_KEY_SWEDEN": "mock_api_key",
        "AZURE_OPENAI_API_VERSION": "mock_api_version",
        "OPENAI_API_KEY": "mock_openai_api_key",
        "AZURE_OPENAI_DEPLOYMENT_NAME": "mock_deployment_name",
        "OPENAI_DEPLOYMENT_NAME": "mock_openai_deployment_name"
    }):
        yield

from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization_with_azure():
    with patch('theory_evaluation.llm_handler.AzureOpenAI', autospec=True) as mock_azure_openai:
        with patch('os.getenv', side_effect=lambda key: {
            "AZURE_OPENAI_ENDPOINT_SWEDEN": "mock_endpoint",
            "AZURE_OPENAI_API_VERSION": "mock_api_version",
            "AZURE_OPENAI_DEPLOYMENT_NAME": "mock_deployment_name"
        }.get(key, None)):
            llm = OpenAI_llm(useAzureOpenAI=True)
            assert llm.azure_endpoint == "mock_endpoint"
            assert llm.api_version == "mock_api_version"
            assert llm.model_name == "mock_deployment_name"
            assert hasattr(llm.client, 'chat')

from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_openai_llm_initialization_without_azure():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        llm = OpenAI_llm(useAzureOpenAI=False)
        assert llm.model_name == "mock_openai_deployment_name"
        assert hasattr(llm.client, 'chat')

from unittest.mock import patch, MagicMock
import json
import pytest

@pytest.mark.asyncio
async def test_openai_json_completion():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content=json.dumps({"answer": "42"})))])

        # Add your test logic here, for example:
        # llm = OpenAI_llm(...)
        # response = await llm._OpenAI_JSON_Completion(...)
        # assert response == {"answer": "42"}

from unittest.mock import patch, AsyncMock, MagicMock
import pytest

@pytest.mark.asyncio
async def test_openai_streaming():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        mock_client = mock_openai.return_value
        mock_stream = AsyncMock()
        mock_stream.__aiter__.return_value = iter([MagicMock(choices=[MagicMock(delta=MagicMock(content="chunk"))])])
        mock_client.chat.completions.create.return_value = mock_stream

        # Add your test logic here, for example:
        # llm = OpenAI_llm(...)
        # async for token in llm.execute():
        #     assert token == "chunk"

from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.asyncio
async def test_openai_chat_completion():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="Hello"))])
        # Add your test logic here

from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.asyncio
async def test_execute_text_generation():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="Hello"))])
        # Add your test logic here

from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.asyncio
async def test_execute_vision():
    with patch('theory_evaluation.llm_handler.OpenAI', autospec=True) as mock_openai:
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="Image response"))])
        # Add the rest of your test logic here
