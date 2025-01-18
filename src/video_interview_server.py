
from flask import Blueprint, request, jsonify, Flask
from flask_socketio import emit
from src import db
from src.models import User
from functools import wraps
import jwt

video_bp = Blueprint('video', __name__)
app = Flask(__name__)
app.register_blueprint(video_bp)

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

@video_bp.route('/start-interview', methods=['POST'])
@token_required
def start_interview(current_user):
    if current_user.role != 'candidate':
        return jsonify({'error': 'Unauthorized'}), 403
    return jsonify({'status': 'success', 'message': 'Interview started'})

@video_bp.route('/end-interview', methods=['POST'])
@token_required
def end_interview(current_user):
    if current_user.role != 'candidate':
        return jsonify({'error': 'Unauthorized'}), 403
    return jsonify({'status': 'success', 'message': 'Interview ended'})

def socket_auth(auth):
    try:
        token = auth.get('token')
        if not token:
            return False
        jwt.decode(token, "your-secret-key", algorithms=["HS256"])
        return True
    except:
        return False
