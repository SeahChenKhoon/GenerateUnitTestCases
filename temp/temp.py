import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import models

def test_delete_user_performance_not_exists(mock_session):
    mock_db = MagicMock()
    mock_session.return_value.__enter__.return_value = mock_db
    mock_query = MagicMock()
    mock_db.query.return_value.filter.return_value = mock_query
    mock_query.all.return_value = []
