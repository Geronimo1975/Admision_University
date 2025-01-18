from flask import render_template
from src import create_app
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/agent-dashboard')
def agent_dashboard():
    return render_template('agent_dashboard.html')

@app.route('/gdpr-dashboard')
def gdpr_dashboard():
    return render_template('gdpr_dashboard.html')

@app.route('/university-dashboard')
def university_dashboard():
    return render_template('university_dashboard.html')

@app.route('/video-interview')
def video_interview():
    return render_template('video_interview.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)