
import unittest
from src.university_portal import app
from src.models import db, University

class TestUniversityPortal(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_university(self):
        response = self.app.post('/universities', json={
            "user_id": 1,
            "name": "Test University",
            "requirements": "Test Requirements"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.get_json()["message"].lower())

    def test_update_requirements(self):
        # First add a university
        self.app.post('/universities', json={
            "user_id": 1,
            "name": "Test University",
            "requirements": "Old Requirements"
        })
        # Then update its requirements
        response = self.app.put('/universities/1', json={
            "requirements": "New Requirements"
        })
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
