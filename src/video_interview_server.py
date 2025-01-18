
from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/start-interview', methods=['POST'])
def start_interview():
    return jsonify({'status': 'success'})

@app.route('/end-interview', methods=['POST'])
def end_interview():
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    socketio.run(app)
