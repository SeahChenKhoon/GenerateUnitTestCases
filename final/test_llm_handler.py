
import pytest


from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_stream = [MagicMock(choices=[MagicMock(delta=MagicMock(content="chunk1"))]),
                   MagicMock(choices=[MagicMock(delta=MagicMock(content="chunk2"))])]

import pytest

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "response content"
