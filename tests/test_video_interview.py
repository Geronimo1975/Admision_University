import unittest
from src.video_interview_server import app

class TestVideoInterview(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True

    def test_generate_question(self):
        response = self.app.post("/question_request", json={"user_id": "123"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("question", response.get_json())

if __name__ == "__main__":
    unittest.main()