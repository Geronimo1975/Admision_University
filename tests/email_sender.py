
import unittest
from unittest.mock import patch
from src.email_sender import send_email

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        self.test_email = "test@example.com"
        self.test_subject = "Test Subject"
        self.test_message = "Test message content."

    @patch('src.email_sender.smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        instance = mock_smtp.return_value
        instance.send_message.return_value = {}
        
        result = send_email(
            self.test_email,
            self.test_subject,
            self.test_message
        )
        self.assertIsNone(result)
        self.assertTrue(instance.send_message.called)

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            send_email("invalid-email", self.test_subject, self.test_message)

if __name__ == "__main__":
    unittest.main()
