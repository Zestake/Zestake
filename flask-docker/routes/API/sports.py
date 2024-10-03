from flask import Blueprint, jsonify
from models import Sport

sports_bp = Blueprint('sports', __name__)

@sports_bp.route("/sports", methods=["POST", "GET"])
def sports():
    from app import data_manager
    return jsonify(data_manager.fetch_data(Sport, ["id", "name"]))
