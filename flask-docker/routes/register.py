from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import User, db

register_bp = Blueprint('register', __name__)

# @register_bp.route("/register", methods=['POST'])
# def register_user():
#     try:
#         user_data = request.get_json()
#         new_user = User(
#             username=user_data['username'],
#             email=user_data['email'],
#             password=generate_password_hash(user_data['password'])
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify({'message': 'User registered successfully'}), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

