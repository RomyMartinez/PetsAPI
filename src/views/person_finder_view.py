from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface):
        self.controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        person_id = request.param['person_id']
        body_response = self.controller.find_person(person_id)

        return HttpResponse(status_code=200, body= body_response)
