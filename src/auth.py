
from flask import Flask, request, jsonify
from models import db, User
import jwt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your-secret-key"

db.init_app(app)

@app.route("/register", methods=["POST"])
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

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.password == data["password"]:
        token = jwt.encode({"user_id": user.id}, app.config["SECRET_KEY"])
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
