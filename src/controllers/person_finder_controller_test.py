#pylint: disable=W0613
import pytest
from .person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository:
    def get_person(self, person_id: int) -> dict:
        return MockPerson(
            first_name="romy",
            last_name="Eduardo",
            pet_name="belinha",
            pet_type="dog"
        )

class MockPeopleRepositoryNoResult:
    def get_person(self, person_id: int) -> None:
        return None

def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(1)

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "romy",
                "last_name": "Eduardo",
                "pet_name": "belinha",
                "pet_type": "dog"
            }
        }
    }

    assert response == expected_response

def test_find_not_found():
    controller = PersonFinderController(MockPeopleRepositoryNoResult())

    with pytest.raises(Exception):
        controller.find(2)
