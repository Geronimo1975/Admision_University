
from flask import Blueprint, request, redirect
from models import db, GDPRConsent

gdpr_bp = Blueprint('gdpr', __name__)

@gdpr_bp.route("/gdpr/consent", methods=["POST"])
def submit_consent():
    consent = GDPRConsent(
        consent_recording=request.form.get("consent_recording") == "on",
        consent_data=request.form.get("consent_data") == "on"
    )
    db.session.add(consent)
    db.session.commit()
    return redirect("/"), 302
