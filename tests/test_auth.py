<<<<<<< HEAD

import unittest
from src.auth import *  # Import your auth module

class TestAuth(unittest.TestCase):
    def test_user_login(self):
        # Add your test logic here
        pass

    def test_user_registration(self):
        # Add your test logic here
        pass

    def test_password_validation(self):
        # Add your test logic here
        pass
=======
import pytest
from auth import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_register(client):
    response = client.post("/register", json={"email": "test@example.com", "password": "123456", "role": "candidate"})
    assert response.status_code == 200

def test_login(client):
    response = client.post("/login", json={"email": "test@example.com", "password": "123456"})
    assert response.status_code == 200
    assert "token" in response.get_json()
>>>>>>> 484d55e (Update)
