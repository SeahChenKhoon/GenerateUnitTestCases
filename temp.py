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
from uuid import UUID
from pydantic import EmailStr
from theory_evaluation.utils import (
from theory_evaluation import models

def test_delete_user_performance_not_found():
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.all.return_value = []
