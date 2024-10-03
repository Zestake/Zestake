from flask import Blueprint, jsonify
from models import Group

groups_bp = Blueprint('groups', __name__)

@groups_bp.route("/groups", methods=["POST", "GET"])
def groups():
    from app import data_manager
    return jsonify(data_manager.fetch_data(Group, ["id", "name", "users"]))
