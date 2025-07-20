from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_conection_handler
from src.controllers.person_finder_controller import PersonFinderController
from src.views.person_finder_view import PersonFinderView

def person_finder_composer():
    model = PeopleRepository(db_conection_handler)
    controller = PersonFinderController(model)
    view = PersonFinderView(controller)

    return view
