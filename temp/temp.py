import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import models

def test_delete_user_performance_operational_error():
    with patch("theory_evaluation.utils.get_db") as mock_get_db:
        mock_get_db.side_effect = OperationalError("Test", "Test", "Test")
        result = delete_user_performance(
            "test@example.com", UUID("12345678-1234-5678-1234-567812345678")
        )
        assert result is False
