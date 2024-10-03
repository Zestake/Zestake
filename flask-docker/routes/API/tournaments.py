from flask import Blueprint, jsonify
from models import Tournament

tournaments_bp = Blueprint('tournaments', __name__)

@tournaments_bp.route("/tournaments", methods=["POST", "GET"])
def tournaments():
        from app import data_manager
        return jsonify(
        data_manager.fetch_data(
            Tournament,
            [
                "id",
                "groups_id",
                "sports_id",
                "name",
                "start_date",
                "end_date",
                "match_value_map",
                "visibility_bets",
            ],
        )
    )
