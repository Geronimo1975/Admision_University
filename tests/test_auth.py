
import unittest
from tests.base import TestBase
from src.auth import auth_bp
from src.models import User, db

class TestAuth(TestBase):
    def setUp(self):
        super().setUp()
        self.app.register_blueprint(auth_bp)
        with self.app.app_context():
            db.create_all()

    def test_register_success(self):
        response = self.client.post("/register", json={
            "email": "test@example.com",
            "password": "Test123!",
            "role": "candidate"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    def test_register_duplicate_email(self):
        # First registration
        self.client.post("/register", json={
            "email": "test@example.com",
            "password": "Test123!",
            "role": "candidate"
        })
        # Duplicate registration
        response = self.client.post("/register", json={
            "email": "test@example.com",
            "password": "Test123!",
            "role": "candidate"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_login_success(self):
        # Register first
        self.client.post("/register", json={
            "email": "test@example.com",
            "password": "Test123!",
            "role": "candidate"
        })
        # Then login
        response = self.client.post("/login", json={
            "email": "test@example.com",
            "password": "Test123!"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.get_json())

    def test_login_invalid_credentials(self):
        response = self.client.post("/login", json={
            "email": "nonexistent@example.com",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.get_json())

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()
