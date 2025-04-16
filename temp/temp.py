
import pytest
from unittest.mock import MagicMock


# New Test Case
import pytest
from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_OpenAI_llm_execute():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = AsyncMock()
    mock_client.chat.completions.create.return_value.choices = [
        MagicMock(message=MagicMock(content=json.dumps({"answer": "7", "explanation": "2+5 equals 7"})))
    ]

    with patch('openai.OpenAI', return_value=mock_client):
        llm = OpenAI_llm(message="What is 2+5?", output="json")
        responses = []
        async for response in llm.execute():
            responses.append(response)

    assert responses == [{"answer": "7", "explanation": "2+5 equals 7"}]
