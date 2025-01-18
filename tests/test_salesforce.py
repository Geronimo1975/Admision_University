
import unittest
from unittest.mock import patch
from src.salesforce import save_interview_result

class TestSalesforce(unittest.TestCase):
    @patch('src.salesforce.Salesforce')
    def test_save_interview_result(self, mock_sf):
        result = save_interview_result("test_candidate", "test_score")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
