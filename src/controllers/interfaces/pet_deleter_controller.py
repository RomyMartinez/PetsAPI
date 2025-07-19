from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):
    @abstractmethod
    def delete(self, pet_name: str) -> None:
        pass
