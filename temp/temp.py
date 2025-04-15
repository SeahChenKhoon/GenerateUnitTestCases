import pytest
from unittest.mock import AsyncMock
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_openai_llm_execute_vision_mode(mock_openai_client):
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = "Vision response"
    mock_openai_client.return_value.chat.completions.create.return_value = mock_response

    llm = OpenAI_llm(
        message="Test message",
        useAzureOpenAI=False,
        output=None,
        mode="vision",
        image_input="test_image_data"
    )

    responses = []
    async for response in llm.execute():
        responses.append(response)

    assert responses == ["Vision response"]
