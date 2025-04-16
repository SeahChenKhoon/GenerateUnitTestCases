
import pytest


# New Test Case
import pytest
import pytest_asyncio

@pytest_asyncio.fixture
async def mock_openai():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=json.dumps({"answer": "7", "explanation": "2+5 equals 7"})))]
    )
    return mock_client

@pytest.mark.asyncio
async def test_openai_llm_execute(mock_openai):
    llm = OpenAI_llm(message="What is 2+5?", useAzureOpenAI=False, output="json")
    llm.client = mock_openai

    responses = []
    async for response in llm.execute():
        responses.append(response)

    assert len(responses) == 1
    assert responses[0] == {"answer": "7", "explanation": "2+5 equals 7"}
