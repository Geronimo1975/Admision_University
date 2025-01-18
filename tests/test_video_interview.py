
import unittest
from unittest.mock import patch
from src.video_interview_server import app

class TestVideoInterview(unittest.TestCase):
    @patch('src.salesforce.Salesforce')
    def setUp(self, mock_sf):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_start_interview(self):
        response = self.app.post('/start-interview', json={
            "candidate_id": "test123",
            "interview_type": "general"
        })
        self.assertEqual(response.status_code, 200)

    def test_end_interview(self):
        response = self.app.post('/end-interview', json={
            "interview_id": "test123"
        })
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
