from flask import Blueprint, jsonify

pets_routes_bp = Blueprint("pets", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"Ola": "Mundo"}), 200
