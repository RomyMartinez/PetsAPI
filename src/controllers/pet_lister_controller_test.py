from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="belinha", type="dog"),
            PetsTable(name="bela", type="cat")
        ]

def test_list():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "belinha", "type": "dog" },
                { "name": "bela", "type": "cat" }
            ]
        }
    }

    assert response == expected_response
