
import pytest
from unittest.mock import MagicMock


@pytest.mark.asyncio
async def test_execute_vision():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision response"
