import argparse
from flask import Flask
from src.models import db
from src.config_loader import load_yaml
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

# Încarcă configurația bazei de date
settings = load_yaml("config/settings.yaml")

# Inițializează aplicația Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = settings["database"]["uri"]

db.init_app(app)

def start_app():
    """Pornește aplicația Flask"""
    app.run(debug=True, port=5000)

def init_db():
    """Inițializează baza de date"""
    with app.app_context():
        db.create_all()
        print("✅ Baza de date a fost inițializată.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", action="store_true", help="Pornește aplicația")
    parser.add_argument("--init-db", action="store_true", help="Inițializează baza de date")

    args = parser.parse_args()

    if args.start:
        start_app()
    elif args.init_db:
        init_db()
    else:
        print("🔹 Folosește --start sau --init-db")
