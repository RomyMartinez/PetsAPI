#pylint: disable=R0801
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.person_creator_view import PersonCreatorView

class MockPeopleCreatorController():
    def create(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person_info["first_name"],
                    "last_name": person_info["last_name"],
                    "age": person_info["age"],
                    "pet_id": person_info["pet_id"]
                }
            }
        }

def test_create():
    controller = MockPeopleCreatorController()
    view = PersonCreatorView(controller)
    request = HttpRequest(body={
        "first_name": "Romy",
        "last_name": "Silva",
        "age": 10,
        "pet_id": 1
    })
    expected_http_response = HttpResponse(status_code=201, body= {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "Romy",
                "last_name": "Silva",
                "age": 10,
                "pet_id": 1
            }
        }
    })

    http_response = view.handle(request)

    assert http_response.body == expected_http_response.body
    assert http_response.status_code == expected_http_response.status_code
