
import unittest
from src.evaluation_ai import evaluate_response

class TestAIEvaluation(unittest.TestCase):
    def test_evaluate_response(self):
        response = evaluate_response("Test Candidate", "Am studiat biologia și am experiență în domeniul medical.")
        self.assertIsInstance(response, str)
        self.assertIn("scor", response.lower())

    def test_score_calculation(self):
        response = evaluate_response("Test Candidate", "No relevant experience")
        self.assertIsInstance(response, str)
        self.assertTrue(any(char.isdigit() for char in response))

if __name__ == "__main__":
    unittest.main()
