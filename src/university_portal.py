from flask import Flask
from models import db, University

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

init_app(app)

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