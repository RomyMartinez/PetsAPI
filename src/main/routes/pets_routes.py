from flask import Blueprint, jsonify
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.views.http_types.http_request import HttpRequest

pets_routes_bp = Blueprint("pets", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    view = pet_lister_composer()
    http_response = view.handle(None)

    return jsonify(http_response.body), http_response.status_code

@pets_routes_bp.route("/pets/<int:pet_id>", methods=["DELETE"])
def delete_pet(pet_id):
    http_request = HttpRequest(param={"pet_id": pet_id})
    view = pet_deleter_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
