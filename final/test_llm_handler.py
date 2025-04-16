import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest


import pytest
import os
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.mark.asyncio
async def test_openai_llm_initialization(monkeypatch):
    monkeypatch.setenv("AZURE_OPENAI_API_KEY_SWEDEN", "test_api_key")
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT_SWEDEN", "https://example.com")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "v1")
    monkeypatch.setenv("AZURE_OPENAI_DEPLOYMENT_NAME", "test-model")

    llm = OpenAI_llm(
        useAzureOpenAI=True,
        azure_endpoint="https://example.com",
        message="Test message",
        image_input=None,
        api_version="v1",
        model_name="test-model",
        max_retries=3,
        output="json",
        mode="text_generation",
        config={"temperature": 0.5},
        verbose=True,
    )
    assert llm.message == "Test message"
    assert llm.azure_endpoint == "https://example.com"
    assert llm.api_version == "v1"
    assert llm.model_name == "test-model"
    assert llm.max_retries == 3
    assert llm.output == "json"
    assert llm.mode == "text_generation"
    assert llm.config == {"temperature": 0.5}
    assert llm.verbose is True
