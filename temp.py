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
from unittest.mock import patch, MagicMock, call
from uuid import UUID
from theory_evaluation.utils import (
from theory_evaluation import models
import pydantic

def test_delete_user_performance():
    mock_performance = MagicMock()
    with patch("theory_evaluation.utils.get_db") as mock_get_db:
        mock_session = mock_get_db.return_value.__enter__.return_value
        mock_session.query.return_value.filter.return_value.all.return_value = [mock_performance]
        result = delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678"))
        assert result is True
        mock_session.delete.assert_has_calls([call(mock_performance)])
