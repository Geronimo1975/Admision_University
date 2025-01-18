import os
import sys

# Adaugă `src/` în calea de import
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Inițializează baza de date (dacă este cazul)
from .models import db
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config_loader.settings")
    db.init_app(app)
    return app
