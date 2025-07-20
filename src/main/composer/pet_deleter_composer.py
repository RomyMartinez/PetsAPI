from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_conection_handler
from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.pet_deleter_view import PetDeleterView

def pet_deleter_composer():
    repository = PetsRepository(db_conection_handler)
    controller = PetDeleterController(repository)
    view = PetDeleterView(controller)

    return view
