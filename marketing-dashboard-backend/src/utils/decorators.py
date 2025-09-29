from functools import wraps
from flask import request, jsonify, g
from src.utils.jwt_utils import decode_token

def auth_required(view_function):
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"message": "missing or invalid authorization header"}), 401
        token = auth_header.split(" ", 1)[1]
        try:
            payload = decode_token(token)
        except Exception as exc:
            return jsonify({"message": "invalid token", "detail": str(exc)}), 401

        g.user = payload
        return view_function(*args, **kwargs)
    return wrapper
