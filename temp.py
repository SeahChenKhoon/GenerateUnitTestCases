import pytest
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
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from theory_evaluation.utils import (
from uuid import UUID
import pydantic

def test_delete_user_performance_not_found():
    mock_session = MagicMock()
    mock_session.query().filter().all.return_value = []
    with patch("theory_evaluation.utils.get_db") as mock_get_db:
        mock_get_db.return_value.__enter__.return_value = mock_session
        result = delete_user_performance("test@example.com", UUID("12345678123456781234567812345678"))
        assert result is False
