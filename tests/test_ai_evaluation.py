<<<<<<< HEAD

import unittest
from src.ai_evaluation import *  # Import your ai_evaluation module

class TestAIEvaluation(unittest.TestCase):
    def test_candidate_evaluation(self):
        # Add your test logic here
        pass

    def test_score_calculation(self):
        # Add your test logic here
        pass
=======
import unittest
from src.evaluation_ai import evaluate_response

class TestAIEvaluation(unittest.TestCase):
    def test_evaluate_response(self):
        response = evaluate_response("Test Candidate", "Am studiat biologia și am experiență în domeniul medical.")
        self.assertIsInstance(response, str)
        self.assertIn("scor", response.lower())

if __name__ == "__main__":
    unittest.main()
>>>>>>> 484d55e (Update)
