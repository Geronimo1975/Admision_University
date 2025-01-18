
from flask import Blueprint, request, jsonify, render_template
from src import db
from src.models import University, User
from functools import wraps
import jwt

university_bp = Blueprint('university', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        try:
            data = jwt.decode(token.split()[1], "your-secret-key", algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'error': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@university_bp.route("/universities", methods=["POST"])
@token_required
def add_university(current_user):
    if current_user.role != 'university':
        return jsonify({'error': 'Unauthorized'}), 403
        
    data = request.get_json()
    new_university = University(
        user_id=current_user.id,
        name=data["name"],
        requirements=data["requirements"]
    )
    db.session.add(new_university)
    db.session.commit()
    return jsonify({"message": "University added successfully!"})

@university_bp.route("/universities/<int:id>", methods=["PUT"])
@token_required
def update_requirements(current_user, id):
    university = University.query.get(id)
    if not university:
        return jsonify({"error": "University not found"}), 404
    if university.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
        
    university.requirements = request.json["requirements"]
    db.session.commit()
    return jsonify({"message": "Requirements updated!"})

@university_bp.route("/dashboard")
@token_required
def dashboard(current_user):
    if current_user.role != 'university':
        return jsonify({'error': 'Unauthorized'}), 403
    universities = University.query.filter_by(user_id=current_user.id).all()
    return render_template('university_dashboard.html', universities=universities)
