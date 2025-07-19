from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorView(ViewInterface):

    def __init__(self, controller: PersonCreatorControllerInterface):
        self.controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        person_info = request.body
        body_response = self.controller.create(person_info)

        return HttpResponse(status_code=201, body= body_response)
