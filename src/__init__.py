from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'test-secret-key'
    db.init_app(app)

    from .auth import auth_bp
    from .gdpr import gdpr_bp
    from .university_portal import university_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(gdpr_bp)
    app.register_blueprint(university_bp)

    with app.app_context():
        db.create_all()

    return app