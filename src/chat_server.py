from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import openai
from salesforce import save_chat_to_crm

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
openai.api_key = "YOUR_OPENAI_API_KEY"

active_chats = {}  # Stocăm utilizatorii în așteptare pentru agenți umani

@app.route("/")
def index():
    return render_template("chat.html")

@socketio.on("message")
def handle_message(data):
    user_id = data["user_id"]
    message = data["message"]

    if user_id in active_chats:
        # Trimitere mesaj către agent uman
        emit("agent_message", {"user_id": user_id, "message": message}, room="agents")
    else:
        # AI răspunde utilizatorului
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )["choices"][0]["message"]["content"]

        # Dacă AI nu știe răspunsul, trimite la un agent uman
        if "Nu sunt sigur" in response:
            active_chats[user_id] = message
            emit("ai_message", {"message": "Un agent uman va prelua conversația în scurt timp."}, room=user_id)
            emit("new_chat", {"user_id": user_id, "message": message}, room="agents")
        else:
            emit("ai_message", {"message": response}, room=user_id)
            save_chat_to_crm(user_id, message, response)

@socketio.on("join_agent")
def join_agent():
    join_room("agents")
    emit("agent_joined", {"message": "Agenții umani s-au conectat."}, room="agents")

@socketio.on("agent_response")
def agent_response(data):
    user_id = data["user_id"]
    message = data["message"]
    emit("agent_message", {"message": message}, room=user_id)

@socketio.on("join")
def on_join(data):
    user_id = data["user_id"]
    join_room(user_id)

@socketio.on("leave")
def on_leave(data):
    user_id = data["user_id"]
    leave_room(user_id)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5003)
