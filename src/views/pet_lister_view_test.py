from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.pet_lister_view import PetListerView

class MockPetsListerController():
    def list_pets(self) -> dict:
        return {
            "data": {
                "type": "Pets",
                "count": 2,
                "attributes": [
                    { "name": "belinha", "type": "dog" },
                    { "name": "bela", "type": "cat" }
                ]
            }
        }

def test_list():
    controller = MockPetsListerController()
    view = PetListerView(controller)
    http_request = HttpRequest()
    expected_http_response = HttpResponse(status_code=200, body= {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "belinha", "type": "dog" },
                { "name": "bela", "type": "cat" }
            ]
        }
    })

    http_response = view.handle(http_request)

    assert http_response.body == expected_http_response.body
    assert http_response.status_code == expected_http_response.status_code
