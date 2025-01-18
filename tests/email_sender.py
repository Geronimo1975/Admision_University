import pytest
from src.email_sender import send_email

class TestEmailSender(pytest.TestCase):
    def test_send_email(self):
        response = send_email("test@example.com", "Test", "Acesta este un test.")
        self.assertIsNone(response)  # Funcția returnează None dacă e-mailul e trimis cu succes

if __name__ == "__main__":
    pytest.main()
