<<<<<<< HEAD

from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

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
    app.run(host='0.0.0.0', port=3000)
=======
from flask import Flask
from config_loader import settings
from models import db

app = Flask(__name__)
app.config.from_mapping(settings)

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 484d55e (Update)
