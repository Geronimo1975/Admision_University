
import unittest
from src.auth import app
from src.models import db, User

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        with app.app_context():
            response = self.app.post("/register", json={
                "email": "test@example.com",
                "password": "123456",
                "role": "candidate"
            })
            self.assertEqual(response.status_code, 200)

    def test_login(self):
        with app.app_context():
            # First register a user
            self.app.post("/register", json={
                "email": "test@example.com",
                "password": "123456",
                "role": "candidate"
            })
            # Then try to login
            response = self.app.post("/login", json={
                "email": "test@example.com",
                "password": "123456"
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn("token", response.get_json())

if __name__ == "__main__":
    unittest.main()
