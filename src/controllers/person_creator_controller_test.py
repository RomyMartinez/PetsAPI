import pytest
from .person_creator_cotroller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

def test_create():
    person_infor = {
        "first_name": "romy",
        "last_name": "Eduardo",
        "age": 10,
        "pet_id": 1
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_infor)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infor


def test_create_invalid_name():
    person_infor = {
        "first_name": "romy312312",
        "last_name": "Eduardo",
        "age": 10,
        "pet_id": 1
    }

    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person_infor)
