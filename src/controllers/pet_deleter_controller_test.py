from unittest import mock
from .pet_deleter_controller import PetDeleterController

def test_delete():
    mock_pets_repository = mock.MagicMock()
    controller = PetDeleterController(mock_pets_repository)
    controller.delete("belinha")

    mock_pets_repository.delete_pet.assert_called_once_with("belinha")
