<<<<<<< HEAD

import unittest
from src.salesforce import *  # Import your salesforce module

class TestSalesforce(unittest.TestCase):
    def test_data_sync(self):
        # Add your test logic here
        pass

    def test_record_creation(self):
        # Add your test logic here
        pass
=======
import unittest
from src.salesforce import save_interview_result

class TestSalesforceIntegration(unittest.TestCase):
    def test_save_interview_result(self):
        response = save_interview_result("Test Candidate", "Test answer", "Scor 8/10")
        self.assertIsNotNone(response)  # Verifică dacă răspunsul este salvat corect

if __name__ == "__main__":
    unittest.main()
>>>>>>> 484d55e (Update)
