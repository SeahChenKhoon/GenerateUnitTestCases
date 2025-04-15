import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest

from unittest.mock import patch
import os
import pytest
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch.dict(os.environ, {"AZURE_OPENAI_ENDPOINT_SWEDEN": "test_endpoint", "AZURE_OPENAI_API_VERSION": "v1", "OPENAI_API_KEY": "test_key"}):
        
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.azure_endpoint == "test_endpoint"
        assert llm.api_version == "v1"
        assert hasattr(llm, "client")
        assert mock_azure_openai.called