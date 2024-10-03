from flask import Blueprint, jsonify
from models import Match

matches_bp = Blueprint('matches', __name__)

@matches_bp.route("/matches", methods=["POST", "GET"])
def matches():
    from app import data_manager
    return jsonify(
        data_manager.fetch_data(
            Match,
            [
                "id",
                "tournament_id",
                "stage",
                "contestants",
                "score",
                "delay",
                "start_date",
            ],
        )
    )
