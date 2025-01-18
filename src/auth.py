
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
from src.models import User
import jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400
        
    user = User(
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data["role"]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registration successful"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    
    if user and check_password_hash(user.password, data["password"]):
        token = jwt.encode(
            {"user_id": user.id}, 
            "your-secret-key",
            algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
