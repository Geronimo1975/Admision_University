from config_loader import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize database here

# Now, other files should import `db` from models.py



class GDPRConsent(db.Model):
    __tablename__ = "gdpr_consent"
    __table_args__ = {"extend_existing": True}  # Previne conflictul

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    consent_recording = db.Column(db.Boolean, default=False)
    consent_data = db.Column(db.Boolean, default=False)

