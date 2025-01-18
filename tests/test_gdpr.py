import unittest
from src.gdpr import app
from src.models import db, GDPRConsent as Consent

class TestGDPR(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        with app.app_context():
            db.init_app(app)
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_submit_consent(self):
        response = self.app.post('/gdpr/consent', data={
            'consent_recording': 'on',
            'consent_data': 'on'
        })
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()