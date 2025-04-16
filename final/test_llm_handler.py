import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm
import pytest
@pytest.fixture
def mock_openai():
    with patch("theory_evaluation.llm_handler.OpenAI") as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock:
        yield mock
