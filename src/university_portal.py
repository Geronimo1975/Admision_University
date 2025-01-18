from flask import Flask, request, jsonify
from models import db, University

app = Flask(__name__)

@app.route("/universities", methods=["POST"])
def add_university():
    data = request.json
    new_university = University(
        user_id=data["user_id"], name=data["name"], requirements=data["requirements"]
    )
    db.session.add(new_university)
    db.session.commit()
    return jsonify({"message": "University added successfully!"})

@app.route("/universities/<int:id>", methods=["PUT"])
def update_requirements(id):
    university = University.query.get(id)
    if not university:
        return jsonify({"error": "University not found"}), 404
    university.requirements = request.json["requirements"]
    db.session.commit()
    return jsonify({"message": "Requirements updated!"})
