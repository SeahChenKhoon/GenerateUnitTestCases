from unittest.mock import patch
@pytest.fixture
def mock_openai():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock:
        yield mock

@pytest.fixture
def mock_azure_openai():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock:
        yield mock
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_execute_vision(mock_openai):
    mock_response = AsyncMock()
    mock_response.choices[0].message.content = "vision content"
    mock_openai.return_value.chat.completions.create.return_value = mock_response
