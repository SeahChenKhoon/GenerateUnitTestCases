import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('os.getenv', side_effect=lambda key: f'mock_{key}'):
        
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.client == mock_azure_openai.return_value
        assert llm.azure_endpoint == 'mock_AZURE_OPENAI_ENDPOINT_SWEDEN'
        assert llm.api_version == 'mock_AZURE_OPENAI_API_VERSION'
        assert llm.model_name == 'mock_AZURE_OPENAI_DEPLOYMENT_NAME'

def test_openai_chat_completion():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client') as mock_client:
        mock_response = AsyncMock()
        mock_response.choices = [AsyncMock()]
        mock_response.choices[0].message.content = "chat completion content"
        mock_client.chat.completions.create.return_value = mock_response

def test_execute_text_generation():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]

def test_execute_vision():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run', new_callable=AsyncMock) as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]
