from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface):
        self.controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        pet_name = request.param['pet_name']
        self.controller.delete(pet_name)

        return HttpResponse(status_code=204)
