import pytest
from unittest.mock import patch
from theory_evaluation.main import shutdown_event

@pytest.mark.asyncio
async def test_shutdown_event():
    with patch('theory_evaluation.main.logger') as mock_logger:
        await shutdown_event()
        assert mock_logger.info.called
        assert mock_logger.info.call_args_list[0][0][0] == "Shutting down the FastAPI application"