
import asyncio
import json
import os
import pytest
from unittest.mock import patch
from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm


from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.os.getenv', return_value='test_value'):
        pass
