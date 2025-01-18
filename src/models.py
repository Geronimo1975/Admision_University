
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)

class GDPRConsent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consent_recording = db.Column(db.Boolean, default=False)
    consent_data = db.Column(db.Boolean, default=False)

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    requirements = db.Column(db.Text)
