
from flask import Blueprint, request, jsonify
from models import db, User
import jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = User(
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registration successful"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.password == data["password"]:
        token = jwt.encode({"user_id": user.id}, "your-secret-key")
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
