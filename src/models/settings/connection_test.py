import pytest
from sqlalchemy import Engine
from .connection import db_conection_handler

@pytest.mark.skip(reason="Skipping test_connect_to_db")
def test_connect_to_db():
    assert db_conection_handler.get_engine() is None

    db_conection_handler.connect_to_db()
    db_engine = db_conection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
