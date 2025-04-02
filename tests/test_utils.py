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
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from uuid import UUID
from theory_evaluation.utils import get_db, validate_user, get_marking_scheme, get_user_performance, manage_user_performance, delete_user_performance
from . import models


@patch("theory_evaluation.utils.get_db")
def test_get_db_success(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    with get_db() as db:
        assert db is session


@patch("theory_evaluation.utils.get_db")
def test_get_db_failure(mock_get_db):
    mock_get_db.side_effect = OperationalError("test", "test", "test")
    with pytest.raises(OperationalError):
        with get_db() as db:
            pass


@patch("theory_evaluation.utils.get_db")
def test_validate_user_exists(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    session.query.return_value.filter.return_value.first.return_value = MagicMock()
    assert validate_user("test@example.com") is True


@patch("theory_evaluation.utils.get_db")
def test_validate_user_does_not_exist(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    session.query.return_value.filter.return_value.first.return_value = None
    assert validate_user("test@example.com") is False


@patch("theory_evaluation.utils.get_db")
def test_validate_user_operational_error(mock_get_db):
    mock_get_db.side_effect = OperationalError("test", "test", "test")
    assert validate_user("test@example.com") is None


@patch("theory_evaluation.utils.get_db")
def test_validate_user_sqlalchemy_error(mock_get_db):
    mock_get_db.side_effect = SQLAlchemyError("test")
    assert validate_user("test@example.com") is None


@patch("theory_evaluation.utils.get_db")
def test_get_marking_scheme_success(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    curriculum = MagicMock(question="Q1", marking_scheme="MS1", model_answer="MA1")
    session.query.return_value.filter.return_value.first.return_value = curriculum
    assert get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678")) == ("Q1", "MS1", "MA1")


@patch("theory_evaluation.utils.get_db")
def test_get_marking_scheme_failure(mock_get_db):
    mock_get_db.side_effect = OperationalError("test", "test", "test")
    assert get_marking_scheme(UUID("12345678-1234-5678-1234-567812345678")) == (None, None, None)


@patch("theory_evaluation.utils.get_db")
def test_get_user_performance_success(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    user_performance = MagicMock(user_attempts=3, llm_evaluation="Good", user_grade="Pass", llm_evaluation_status=1)
    session.query.return_value.filter.return_value.order_by.return_value.first.return_value = user_performance
    assert get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678")) == (3, "Good", "Pass", 1)


@patch("theory_evaluation.utils.get_db")
def test_get_user_performance_failure(mock_get_db):
    mock_get_db.side_effect = OperationalError("test", "test", "test")
    assert get_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678")) == (0, "An unexpected error occurred. Please try again.", "No grade available.", 0)


@patch("theory_evaluation.utils.get_db")
def test_manage_user_performance_create_new_attempt(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    session.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
    assert manage_user_performance(0, "test@example.com", UUID("12345678-1234-5678-1234-567812345678"), "response") is True


@patch("theory_evaluation.utils.get_db")
def test_delete_user_performance_success(mock_get_db):
    session = MagicMock()
    mock_get_db.return_value.__enter__.return_value = session
    session.query.return_value.filter.return_value.all.return_value = [MagicMock()]
    assert delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678")) is True


@patch("theory_evaluation.utils.get_db")
def test_delete_user_performance_failure(mock_get_db):
    mock_get_db.side_effect = OperationalError("test", "test", "test")
    assert delete_user_performance("test@example.com", UUID("12345678-1234-5678-1234-567812345678")) is False
```