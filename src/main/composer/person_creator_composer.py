from src.models.sqlite.settings.connection import db_conection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_creator_controller import PersonCreatorController
from src.views.person_creator_view import PersonCreatorView

def person_creator_composer():
    model = PeopleRepository(db_conection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)

    return view
