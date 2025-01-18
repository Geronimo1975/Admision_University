from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from salesforce import save_call_to_crm
from gdpr import GDPRConsent, db

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice_reply():
    user_phone = request.values.get("From", "")
    consent = GDPRConsent.query.filter_by(email=user_phone).first()

    response = VoiceResponse()

    if consent and consent.consent_recording:
        response.say("Apelul tău va fi înregistrat pentru îmbunătățirea serviciului.")
        response.record(timeout=30, transcribe=True, play_beep=True, action="/save_recording")
    else:
        response.say("Acest apel nu va fi înregistrat.")
        response.pause(length=2)

    response.say("În ce te pot ajuta?")
    return str(response)

@app.route("/save_recording", methods=["POST"])
def save_recording():
    recording_url = request.values.get("RecordingUrl", "")
    transcript = request.values.get("TranscriptionText", "")
    user_phone = request.values.get("From", "")

    save_call_to_crm(user_phone, recording_url, transcript)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, port=5002)
