from src.controllers.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PetListerView
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_conection_handler

def pet_lister_composer():
    repository = PetsRepository(db_conection_handler)
    controller = PetListerController(repository)
    view = PetListerView(controller)

    return view
