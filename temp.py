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
from theory_evaluation.utils import (
from theory_evaluation import models
from uuid import UUID
import pydantic

def test_init_db_session(monkeypatch):
    monkeypatch.setenv("DB_USER", "user")
    monkeypatch.setenv("DB_PASSWORD", "password")
    monkeypatch.setenv("DB_NAME", "dbname")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("SSL_MODE", "require")
    monkeypatch.setenv("ENVIRONMENT", "local")
