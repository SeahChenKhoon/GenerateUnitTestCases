
from unittest.mock import patch
@pytest.fixture
def mock_openai_llm():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', new_callable=MagicMock) as mock_client:
        yield mock_client

# New Test Case
from openai import OpenAI
from unittest.mock import patch

@pytest.mark.asyncio
async def test_execute():
    with patch.object(OpenAI, 'chat') as mock_chat:
        mock_chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content='{"answer": "7", "explanation": "2+5 equals 7."}'))])
        llm = OpenAI_llm(message="You are a AI teacher in math.", useAzureOpenAI=False, output="json")
        responses = []
        async for response in llm.execute():
            responses.append(response)
        assert responses == [{"answer": "7", "explanation": "2+5 equals 7."}]
