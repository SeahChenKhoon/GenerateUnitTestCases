import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import models
from theory_evaluation.utils import delete_user_performance, get_db, get_marking_scheme, get_user_performance, init_db_session, manage_user_performance, validate_user
import pytest
@pytest.fixture
def mock_db_session():
    with patch('theory_evaluation.utils.get_db') as mock_get_db:
        mock_session = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_session
        yield mock_session

# New Test Case
from unittest import mock
from uuid import UUID
from your_module import delete_user_performance  # Replace with the actual import path

def test_delete_user_performance_not_exists():
    mock_db_session = mock.Mock()
    mock_db_session.query.return_value.filter.return_value.all.return_value = []

    with mock.patch('your_module.get_db', return_value=mock_db_session):
        result = delete_user_performance(email="test@example.com", question_id=UUID("00000000-0000-0000-0000-000000000000"))
        assert result is False
