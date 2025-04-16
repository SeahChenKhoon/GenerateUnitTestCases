
import pytest
from unittest.mock import MagicMock


from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_init():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('os.getenv', return_value='mock_value'):
        llm = OpenAI_llm(useAzureOpenAI=True)
        assert llm.client == mock_azure_openai.return_value

from unittest.mock import MagicMock
import pytest

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices = [MagicMock()]
    mock_chunk.choices[0].delta.content = "streamed content"

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "chat content"
