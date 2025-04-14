import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import models

def test_init_db_session_local(mock_env_vars):
    with patch("theory_evaluation.utils.create_engine") as mock_create_engine:
        init_db_session()
        mock_create_engine.assert_called_once_with(
            "postgresql+psycopg://test_user:test_password@localhost:5432/test_db"
        )
        assert hasattr(theory_evaluation.utils, "SessionLocal")
