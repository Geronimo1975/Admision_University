from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": incoming_msg}]
    )
    msg = MessagingResponse()
    msg.message(response["choices"][0]["message"]["content"])
    return str(msg)

if __name__ == "__main__":
    app.run(port=5001)
