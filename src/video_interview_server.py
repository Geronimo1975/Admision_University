from flask import Blueprint, Flask, request, jsonify
from functools import wraps
import jwt

video_bp = Blueprint('video', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token missing'}), 401
        try:
            data = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
        except:
            return jsonify({'error': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated

@video_bp.route('/start-interview', methods=['POST'])
@token_required
def start_interview():
    return jsonify({'status': 'Interview started'})

@video_bp.route('/end-interview', methods=['POST'])
@token_required
def end_interview():
    return jsonify({'status': 'Interview ended'})