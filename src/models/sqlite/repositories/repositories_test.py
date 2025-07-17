import pytest
from src.models.sqlite.settings.connection import db_conection_handler
from .pets_repository import PetsRepository

db_conection_handler.connect_to_db()

@pytest.mark.skip(reason="Connection to database")
def test_list_pets():
    repo = PetsRepository(db_conection_handler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="Connection to database")
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_conection_handler)
    repo.delete_pet(name)
