
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_openai_client():
    mock_azure = MagicMock()
    mock_openai = MagicMock()
    return mock_azure, mock_openai

def test_openai_llm_initialization(mock_openai_client):
    mock_azure, mock_openai = mock_openai_client
    # Add assertions or test logic here


import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import MagicMock, AsyncMock

@pytest.fixture
def mock_openai_client(monkeypatch):
    mock_openai = MagicMock()
    monkeypatch.setattr('openai.OpenAI', mock_openai)
    return monkeypatch, mock_openai

def test_openai_streaming(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_chunk = MagicMock()
    mock_chunk.choices = [MagicMock(delta=MagicMock(content="streaming content"))]
    mock_openai.return_value.chat.completions.create = AsyncMock(return_value=[mock_chunk])


import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

import pytest
from unittest.mock import MagicMock, AsyncMock

@pytest.fixture
def mock_openai_client():
    mock_openai = MagicMock()
    return None, mock_openai

def test_execute_vision(mock_openai_client):
    _, mock_openai = mock_openai_client
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="vision content"))]
    mock_openai.return_value.chat.completions.create = AsyncMock(return_value=mock_response)

