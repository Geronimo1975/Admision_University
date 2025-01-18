import unittest
from src.gdpr import app, db, GDPRConsent

class TestGDPR(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_gdpr_consent(self):
        response = self.app.post("/gdpr", data={
            "email": "test@example.com",
            "consent_recording": "on",
            "consent_data": "on"
        })
        self.assertEqual(response.status_code, 302)  # Redirect după salvare

if __name__ == "__main__":
    unittest.main()
