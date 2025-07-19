import pytest
from src.models.sqlite.settings.connection import db_conection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

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

@pytest.mark.skip(reason="Connection to database")
def test_insert_people():
    first_name = "romy"
    last_name = "Eduardo"
    age = 10
    pet_id = 1

    repo = PeopleRepository(db_conection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Connection to database")
def test_get_people():
    person_id = 1
    repo = PeopleRepository(db_conection_handler)

    response = repo.get_person(person_id)
    print(response)
