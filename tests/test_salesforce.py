
import unittest
from src.salesforce import save_interview_result

class TestSalesforceIntegration(unittest.TestCase):
    def test_save_interview_result(self):
        response = save_interview_result("Test Candidate", "Test answer", "Scor 8/10")
        self.assertIsNotNone(response)
        
    def test_record_creation(self):
        result = save_interview_result("New Candidate", "Test response", "Scor 9/10")
        self.assertTrue(isinstance(result, dict))
        self.assertIn('id', result)

if __name__ == "__main__":
    unittest.main()
