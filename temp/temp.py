import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import models

def test_init_db_session(mock_env_vars):
    init_db_session()
    from theory_evaluation import utils
    assert hasattr(utils, "SessionLocal")
