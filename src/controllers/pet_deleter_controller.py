from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def delete(self, pet_name: str) -> None:
        self.__pets_repository.delete_pet(pet_name)
