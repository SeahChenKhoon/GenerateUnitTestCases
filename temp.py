import pytest
import os
import time
import pydantic
from uuid import U
from sqlalchemy import c
from sqlalchemy.orm import s
from sqlalchemy.exc import S
from contextlib import c
from theory_evaluation import m
from theory_evaluation.utils import d
import pytest
from unittest.mock import p
from sqlalchemy.exc import S
from theory_evaluation.utils import (
    init_db_session,
    get_db,
    validate_user,
    get_marking_scheme,
    get_user_performance,
    manage_user_performance,
    delete_user_performance,
from theory_evaluation import m
from uuid import U
import pydantic

def test_delete_user_performance_not_exists():
    mock_session = MagicMock()
    mock_session.query.return_value.filter.return_value.all.return_value = []
    with patch("theory_evaluation.utils.SessionLocal", return_value=mock_session):
        result = delete_user_performance(
            email=pydantic.EmailStr("test@example.com"),
            question_id=UUID("12345678123456781234567812345678")
        )
        assert result is False
