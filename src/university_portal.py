
from flask import Blueprint, request, jsonify
from models import db, University

university_bp = Blueprint('university', __name__)

@university_bp.route("/universities", methods=["POST"])
def add_university():
    data = request.get_json()
    new_university = University(
        user_id=data["user_id"],
        name=data["name"],
        requirements=data["requirements"]
    )
    db.session.add(new_university)
    db.session.commit()
    return jsonify({"message": "University added successfully!"})

@university_bp.route("/universities/<int:id>", methods=["PUT"])
def update_requirements(id):
    university = University.query.get(id)
    if not university:
        return jsonify({"error": "University not found"}), 404
    university.requirements = request.json["requirements"]
    db.session.commit()
    return jsonify({"message": "Requirements updated!"})
