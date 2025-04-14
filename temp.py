import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from . import models

def test_delete_user_performance_not_exists():
    mock_session = MagicMock()
    mock_session.query.return_value.filter.return_value.all.return_value = []
