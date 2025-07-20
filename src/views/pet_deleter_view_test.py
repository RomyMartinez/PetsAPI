from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .pet_deleter_view import PetDeleterView

class MockPetDeleterController():
    def delete(self, person_id: int) -> None:
        pass

def test_delete():
    controller = MockPetDeleterController()
    view = PetDeleterView(controller)
    http_request = HttpRequest(param={"pet_id": 1})
    expected_http_response = HttpResponse(status_code=204)

    http_response = view.handle(http_request)

    assert http_response.status_code == expected_http_response.status_code
