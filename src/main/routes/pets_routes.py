from flask import Blueprint, jsonify
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.views.http_types.http_request import HttpRequest

from src.errors.error_handler import handle_error

pets_routes_bp = Blueprint("pets", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_lister_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_error(error)
        return jsonify(http_response.body), http_response.status_code


@pets_routes_bp.route("/pets/<string:pet_name>", methods=["DELETE"])
def delete_pet(pet_name):
    try:
        http_request = HttpRequest(param={"pet_name": pet_name})
        view = pet_deleter_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_error(error)
        return jsonify(http_response.body), http_response.status_code
