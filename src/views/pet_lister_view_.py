from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_lister_controller import PetListerControllerInterface

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface):
        self.controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        body_response = self.controller.list_pets()

        return HttpResponse(status_code=200, body= body_response)
