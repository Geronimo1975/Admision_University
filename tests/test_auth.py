
import unittest
from src.auth import app

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True

    def test_register(self):
        response = self.app.post("/register", json={
            "email": "test@example.com",
            "password": "123456",
            "role": "candidate"
        })
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.post("/login", json={
            "email": "test@example.com",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.get_json())

if __name__ == "__main__":
    unittest.main()
