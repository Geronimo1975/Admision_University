import os
import yaml
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

settings = load_yaml("config/settings.yaml")

db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/admission_system.db"
    db.init_app(app)
