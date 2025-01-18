from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from src.evaluation_ai import evaluate_response
from salesforce import save_interview_result

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("video_interview.html")

@socketio.on("submit_answer")
def handle_submit_answer(data):
    user_id = data["user_id"]
    answer = data["answer"]

    evaluation = evaluate_response(user_id, answer)
    save_interview_result(user_id, answer, evaluation)

    emit("answer_received", {"message": "Răspuns analizat!", "evaluation": evaluation}, room=user_id)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5006)
