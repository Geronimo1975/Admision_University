from flask import Flask, request, jsonify
from models import db, GDPRConsent

app = Flask(__name__)

@app.route("/gdpr", methods=["POST"])
def gdpr_consent():
    data = request.json
    new_consent = GDPRConsent(email=data["email"], consent_recording=data["consent_recording"], consent_data=data["consent_data"])
    db.session.add(new_consent)
    db.session.commit()
    return jsonify({"message": "GDPR settings updated"})
