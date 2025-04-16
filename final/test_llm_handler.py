
from unittest.mock import patch
@pytest.fixture
def mock_openai_llm():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        yield mock_client

from unittest.mock import patch

@pytest.mark.asyncio
async def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure_openai, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.os.getenv', return_value='mock_value'):
        pass
