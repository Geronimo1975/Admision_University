
import unittest
from src.evaluation_ai import evaluate_response

class TestAIEvaluation(unittest.TestCase):
    def test_evaluate_response(self):
        test_response = "Am experiență în cercetare medicală și biotehnologie."
        result = evaluate_response("Test Candidate", test_response)
        self.assertIsInstance(result, str)
        self.assertIn("Score", result)

    def test_empty_response(self):
        result = evaluate_response("Test Candidate", "")
        self.assertIsInstance(result, str)
        self.assertIn("Score: 0", result)

    def test_invalid_input(self):
        result = evaluate_response("", None)
        self.assertIsInstance(result, str)
        self.assertIn("error", result.lower())

if __name__ == "__main__":
    unittest.main()
