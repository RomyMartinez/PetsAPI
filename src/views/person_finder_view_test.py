#pylint: disable=R0801
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.person_finder_view import PersonFinderView

class MockPeopleFinderController():
    def find_person(self, person_id: int) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": "Romy",
                    "last_name": "Silva",
                    "age": 15,
                    "pet_id": person_id
                }
            }
        }

def test_find():
    controller = MockPeopleFinderController()
    view = PersonFinderView(controller)
    http_request = HttpRequest(param={"person_id": 4})
    expected_http_response = HttpResponse(status_code=200, body= {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "Romy",
                "last_name": "Silva",
                "age": 15,
                "pet_id": 4
            }
        }
    })

    http_response = view.handle(http_request)

    assert http_response.body == expected_http_response.body
    assert http_response.status_code == expected_http_response.status_code
