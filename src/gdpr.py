
from flask import Blueprint, request, jsonify, render_template
from src import db
from src.models import GDPRConsent, User
from functools import wraps
import jwt

gdpr_bp = Blueprint('gdpr', __name__)

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

@gdpr_bp.route("/gdpr/consent", methods=["POST"])
@token_required
def submit_consent(current_user):
    data = request.get_json()
    consent = GDPRConsent(
        user_id=current_user.id,
        consent_recording=data.get("consent_recording", False),
        consent_data=data.get("consent_data", False)
    )
    db.session.add(consent)
    db.session.commit()
    return jsonify({"message": "GDPR consent recorded successfully"})

@gdpr_bp.route("/gdpr/status")
@token_required
def get_consent_status(current_user):
    consent = GDPRConsent.query.filter_by(user_id=current_user.id).first()
    if not consent:
        return jsonify({"consent_recording": False, "consent_data": False})
    return jsonify({
        "consent_recording": consent.consent_recording,
        "consent_data": consent.consent_data
    })
