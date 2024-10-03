from flask import Blueprint, jsonify
from models import User

users_bp = Blueprint('users', __name__)

@users_bp.route("/users", methods=["POST", "GET"])
def users():
    from app import data_manager
    return jsonify(data_manager.fetch_data(User, ["id", "username", "password", "email"]))
