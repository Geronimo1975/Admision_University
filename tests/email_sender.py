
import unittest
from src.email_sender import send_email

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        self.test_email = "test@example.com"
        self.test_subject = "Test"
        self.test_message = "Acesta este un test."

    def test_send_email(self):
        response = send_email(self.test_email, self.test_subject, self.test_message)
        self.assertIsNone(response)  # Function returns None if email is sent successfully

if __name__ == "__main__":
    unittest.main()
