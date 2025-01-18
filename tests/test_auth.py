
from tests.base import TestBase
from src.auth import app as auth_app
from src.models import User

class TestAuth(TestBase):
    def setUp(self):
        super().setUp()
        self.app.register_blueprint(auth_app)

    def test_register(self):
        response = self.client.post("/register", json={
            "email": "test@example.com",
            "password": "123456",
            "role": "candidate"
        })
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # First register a user
        self.client.post("/register", json={
            "email": "test@example.com",
            "password": "123456",
            "role": "candidate"
        })
        # Then try to login
        response = self.client.post("/login", json={
            "email": "test@example.com",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.get_json())

if __name__ == "__main__":
    unittest.main()
