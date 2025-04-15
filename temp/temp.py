import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_llm_openai_chat_completion():
    with patch('theory_evaluation.llm_handler.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value.choices = [MagicMock(message=MagicMock(content='response'))]
        llm = OpenAI_llm(message='Test message')
        result = await llm._OpenAI_Chat_Completion()
        assert result == 'response'
        assert mock_client.chat.completions.create.called
