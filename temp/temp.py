import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import _OpenAI_Chat_Completion, _OpenAI_JSON_Completion, _OpenAI_Streaming, __init__, _run, execute, main
from theory_evaluation.llm_handler import _OpenAI_Chat_Completion



def test_openai_llm_initialization_with_azure(mock_azure_openai, mock_env_vars):
    llm = OpenAI_llm(useAzureOpenAI=True)
    assert llm.client == mock_azure_openai.return_value
    assert llm.model_name == "azure_model"