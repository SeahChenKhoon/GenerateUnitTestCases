import os
import time
import pydantic
from uuid import UUID
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager
from theory_evaluation import modelsfrom unittest.mock import patch
from theory_evaluation.utils import init_db_session
from unittest.mock import MagicMock
from unittest import patch
from unittest import MagicMock
from unittest.mock import patch, MagicMock
from unittest import TestCase
from unittest import TestCase
from unittest.mock import MagicMock
from unittest import patch
from unittest.mock import patch, MagicMock
from unittest.mock import MagicMock
from unittest.mock import patch, MagicMock


def test_delete_user_performance_not_exists():
    with patch("theory_evaluation.utils.get_db") as mock_get_db:
        mock_session = MagicMock()
        mock_get_db.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.filter.return_value.all.return_value = []
