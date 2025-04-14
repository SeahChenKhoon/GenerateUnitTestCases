import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import modelsfrom unittest.mock import patchfrom unittest.mock import MagicMock
from pydantic import EmailStrfrom unittest.mock import MagicMockfrom unittest.mock import MagicMockfrom unittest.mock import MagicMockfrom unittest.mock import MagicMock

def test_delete_user_performance(mock_session):
    mock_db = MagicMock()
    mock_session.return_value.__enter__.return_value = mock_db
    mock_performance = MagicMock()
    mock_db.query.return_value.filter.return_value.all.return_value = [mock_performance]
    
    result = delete_user_performance(
        email=EmailStr("test@example.com"),
        question_id=UUID("12345678-1234-5678-1234-567812345678")
    )
    
    assert result is True
