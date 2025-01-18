
from tests.base import TestBase
from src.university_portal import university_bp as university_app

class TestUniversityPortal(TestBase):
    def setUp(self):
        super().setUp()
        self.app.register_blueprint(university_app)

    def test_add_university(self):
        response = self.client.post("/universities", json={
            "user_id": 1,
            "name": "Test University",
            "requirements": "Test Requirements"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_requirements(self):
        # First add a university
        self.client.post("/universities", json={
            "user_id": 1,
            "name": "Test University",
            "requirements": "Old Requirements"
        })
        # Then update requirements
        response = self.client.put("/universities/1", json={
            "requirements": "New Requirements"
        })
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
