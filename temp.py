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
from theory_evaluation import models
from uuid import UUID
import pydantic

@patch("theory_evaluation.utils.get_db")
def test_delete_user_performance_sqlalchemy_error(mock_get_db, mock_email, mock_uuid):
    mock_get_db.side_effect = SQLAlchemyError("Test")
    result = delete_user_performance(mock_email, mock_uuid)
    assert result is False
