import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision content"
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client.chat.completions.create", return_value=mock_response):
        llm = OpenAI_llm(message="Test message", mode="vision", image_input="image_data")
        async for response in llm.execute():
            assert response == "vision content"
