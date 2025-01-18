
import unittest
from src.university_portal import app
from src.models import db, University

class TestUniversityPortal(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        from models import init_db
        init_db(app)

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_university(self):
        with app.app_context():
            response = self.app.post('/universities', json={
                "user_id": 1,
                "name": "Test University",
                "requirements": "Test Requirements"
            })
            self.assertEqual(response.status_code, 200)

    def test_update_requirements(self):
        with app.app_context():
            self.app.post('/universities', json={
                "user_id": 1,
                "name": "Test University",
                "requirements": "Old Requirements"
            })
            response = self.app.put('/universities/1', json={
                "requirements": "New Requirements"
            })
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
