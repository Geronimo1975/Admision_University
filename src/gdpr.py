
from flask import Flask, request, redirect
from models import db, GDPRConsent

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/gdpr/consent", methods=["POST"])
def submit_consent():
    consent = GDPRConsent(
        consent_recording=request.form.get("consent_recording") == "on",
        consent_data=request.form.get("consent_data") == "on"
    )
    db.session.add(consent)
    db.session.commit()
    return redirect("/"), 302
