from flask import Blueprint, jsonify
from models import Bet

bets_bp = Blueprint('bets', __name__)

@bets_bp.route("/bets", methods=["POST", "GET"])
def bets():
   from app import data_manager
   return jsonify(data_manager.fetch_data(Bet, ["id", "match_id", "user_id", "bet"]))