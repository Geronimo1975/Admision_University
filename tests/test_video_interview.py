<<<<<<< HEAD

import unittest
from src.video_interview_server import *  # Import your video_interview module

class TestVideoInterview(unittest.TestCase):
    def test_video_stream(self):
        # Add your test logic here
        pass

    def test_recording_storage(self):
        # Add your test logic here
        pass
=======
import pytest
from video_interview_server import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_generate_question(client):
    response = client.post("/question_request", json={"user_id": "123"})
    assert response.status_code == 200
    assert "question" in response.get_json()
>>>>>>> 484d55e (Update)
