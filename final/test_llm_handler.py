
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI


import pytest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('os.getenv', return_value='mock_value'):
        llm = OpenAI_llm(
            useAzureOpenAI=True,
            azure_endpoint='mock_endpoint',
            message='Test message',
            image_input='mock_image_input',
            api_version='mock_api_version',
            model_name='mock_model_name',
            max_retries=5,
            output='json',
            mode='text_generation',
            config={'temperature': 0.5},
            verbose=True
        )
        assert llm.message == 'Test message'
        assert llm.image_input == 'mock_image_input'
        assert llm.azure_endpoint == 'mock_endpoint'
        assert llm.api_version == 'mock_api_version'
        assert llm.model_name == 'mock_model_name'
        assert llm.max_retries == 5
        assert llm.output == 'json'
        assert llm.mode == 'text_generation'
        assert llm.config == {'temperature': 0.5}
        assert llm.verbose is True
        assert hasattr(llm, 'client')
        assert mock_azure_openai.called


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_llm_execute_text_generation():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', new_callable=AsyncMock) as mock_run:
        mock_run.return_value = AsyncMock()
        mock_run.return_value.__aiter__.return_value = iter(['response'])
        llm = OpenAI_llm(message='Test message', output='json', mode='text_generation')
        responses = []
        async for response in llm.execute():
            responses.append(response)
        assert responses == ['response']
        assert mock_run.called


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_llm_execute_vision():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', new_callable=AsyncMock) as mock_run:
        mock_run.return_value = AsyncMock()
        mock_run.return_value.__aiter__.return_value = iter(['response'])
        llm = OpenAI_llm(message='Test message', output='json', mode='vision', image_input='mock_image_input')
        responses = []
        async for response in llm.execute():
            responses.append(response)
        assert responses == ['response']
        assert mock_run.called


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_llm_openai_json_completion():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value.choices = [MagicMock(message=MagicMock(content='{"key": "value"}'))]
        llm = OpenAI_llm(message='Test message')
        result = await llm._OpenAI_JSON_Completion()
        assert result == {"key": "value"}
        assert mock_client.chat.completions.create.called


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_llm_openai_streaming():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value = iter([MagicMock(choices=[MagicMock(delta=MagicMock(content='chunk'))])])
        llm = OpenAI_llm(message='Test message')
        result = []
        async for chunk in llm._OpenAI_Streaming():
            result.append(chunk)
        assert result == ['chunk']
        assert mock_client.chat.completions.create.called


import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_llm_openai_chat_completion():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value.choices = [MagicMock(message=MagicMock(content='response'))]
        llm = OpenAI_llm(message='Test message')
        result = await llm._OpenAI_Chat_Completion()
        assert result == 'response'
        assert mock_client.chat.completions.create.called

