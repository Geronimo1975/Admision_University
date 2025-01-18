
from tests.base import TestBase
from src.gdpr import gdpr_bp as gdpr_app

class TestGDPR(TestBase):
    def setUp(self):
        super().setUp()
        self.app.register_blueprint(gdpr_app)

    def test_submit_consent(self):
        response = self.client.post("/gdpr/consent", data={
            "consent_recording": "on",
            "consent_data": "on"
        })
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()
