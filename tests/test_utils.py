import pytest
import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from . import models
from theory_evaluation.utils import delete_user_performance, get_db, get_marking_scheme, get_user_performance, manage_user_performance, validate_user

```python
import pytest
from unittest.mock import patch, MagicMock
from theory_evaluation.utils import get_db, validate_user, get_marking_scheme, get_user_performance, manage_user_performance, delete_user_performance
from . import models
from uuid import UUID
from pydantic import EmailStr
from sqlalchemy.exc import OperationalError, SQLAlchemyError

@pytest.fixture
def mock_session():
    session = MagicMock()
    session.close = MagicMock()
    return session

@pytest.fixture
def mock_scoped_session(mock_session):
    with patch("theory_evaluation.utils.SessionLocal") as mock:
        mock.return_value = mock_session
        yield mock

@pytest.fixture
def mock_engine():
    with patch("theory_evaluation.utils.engine") as mock:
        yield mock

def test_get_db_success(mock_scoped_session, mock_session):
    with get_db() as db:
        assert db is mock_session
    mock_session.close.assert_called_once()

def test_get_db_failure(mock_scoped_session, mock_session):
    mock_session.side_effect = SQLAlchemyError("DB error")
    with pytest.raises(SQLAlchemyError):
        with get_db() as db:
            pass
    mock_session.close.assert_called_once()

def test_validate_user_success(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    mock_query = mock_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_first = mock_filter.first.return_value = MagicMock()
    assert validate_user(email) is True

def test_validate_user_no_user_found(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    mock_query = mock_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_filter.first.return_value = None
    assert validate_user(email) is False

def test_validate_user_operational_error(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    mock_session.query.side_effect = OperationalError("DB connection error")
    assert validate_user(email) is None

def test_validate_user_sqlalchemy_error(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    mock_session.query.side_effect = SQLAlchemyError("Query error")
    assert validate_user(email) is None

def test_get_marking_scheme_success(mock_scoped_session, mock_session):
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_query = mock_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_first = mock_filter.first.return_value = MagicMock(question="Q1", marking_scheme="MS1", model_answer="MA1")
    assert get_marking_scheme(uuid) == ("Q1", "MS1", "MA1")

def test_get_marking_scheme_failure(mock_scoped_session, mock_session):
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_session.query.side_effect = OperationalError("DB connection error")
    assert get_marking_scheme(uuid) == (None, None, None)

def test_get_user_performance_success(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_query = mock_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_order_by = mock_filter.order_by.return_value
    mock_first = mock_order_by.first.return_value = MagicMock(user_attempts=1, llm_evaluation="Good", user_grade="Pass", llm_evaluation_status=1)
    assert get_user_performance(email, uuid) == (1, "Good", "Pass", 1)

def test_get_user_performance_failure(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_session.query.side_effect = OperationalError("DB connection error")
    assert get_user_performance(email, uuid) == (0, "An unexpected error occurred. Please try again.", "No grade available.", 0)

def test_manage_user_performance_success_new_attempt(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    user_response = "Response"
    assert manage_user_performance(0, email, uuid, user_response=user_response) is True

def test_manage_user_performance_failure_sqlalchemy_error(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_session.commit.side_effect = SQLAlchemyError("Commit failed")
    assert manage_user_performance(0, email, uuid, user_response="Response") is False

def test_delete_user_performance_success(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_query = mock_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_all = mock_filter.all.return_value = [MagicMock()]
    assert delete_user_performance(email, uuid) is True

def test_delete_user_performance_failure(mock_scoped_session, mock_session):
    email = EmailStr("test@example.com")
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    mock_session.query.side_effect = OperationalError("DB connection error")
    assert delete_user_performance(email, uuid) is False
```