
from tests.base import TestBase
from src.models import GDPRConsent, db

class TestGDPR(TestBase):
    def test_update_consent(self):
        consent = GDPRConsent(
            consent_recording=True,
            consent_data=True
        )
        with self.app.app_context():
            db.session.add(consent)
            db.session.commit()
            
            response = self.client.post('/gdpr/consent', json={
                'consent_id': consent.id,
                'consent_recording': False,
                'consent_data': True
            })
            self.assertEqual(response.status_code, 200)
            
            updated_consent = GDPRConsent.query.get(consent.id)
            self.assertFalse(updated_consent.consent_recording)
            self.assertTrue(updated_consent.consent_data)

    def test_get_consent(self):
        consent = GDPRConsent(
            consent_recording=True,
            consent_data=True
        )
        with self.app.app_context():
            db.session.add(consent)
            db.session.commit()
            
            response = self.client.get(f'/gdpr/consent/{consent.id}')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertTrue(data['consent_recording'])
            self.assertTrue(data['consent_data'])

if __name__ == '__main__':
    unittest.main()
