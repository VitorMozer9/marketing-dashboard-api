from flask import Blueprint, request, jsonify
from src.services.auth_services import AuthService
from src.utils.jwt_utils import create_token

bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_service = AuthService()

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email", "")
    password = data.get("password", "")
    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    user = auth_service.authenticate(email=email, password=password)
    if not user:
        return jsonify({"message": "invalid credentials"}), 401

    token_payload = {
        "user_id": user.id,
        "email": user.email,
        "role": user.role
    }
    token = create_token(token_payload)
    return jsonify({"access_token": token, "token_type": "bearer"})
