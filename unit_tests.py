import unittest
from unittest.mock import MagicMock
from calculator_code import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.run = MagicMock()  # Mock run method to prevent the app from running during tests

    def test_smoke_test(self):
        self.assertIsInstance(self.calculator, Calculator, "Failed to create a Calculator instance")

    def test_add_to_expression(self):
        self.calculator.add_to_expression("5")
        self.assertEqual(self.calculator.current_expression, "5")

    def test_append_operator(self):
        self.calculator.current_expression = "5"
        self.calculator.append_operator("+")
        self.assertEqual(self.calculator.total_expression, "5+")
        self.assertEqual(self.calculator.current_expression, "")

    def test_clear(self):
        self.calculator.current_expression = "5"
        self.calculator.total_expression = "10+"
        self.calculator.clear()
        self.assertEqual(self.calculator.current_expression, "")
        self.assertEqual(self.calculator.total_expression, "")

    def test_sqrt(self):
        self.calculator.current_expression = "9"
        self.calculator.sqrt()
        self.assertEqual(self.calculator.current_expression, "3.0")

    def test_evaluate(self):
        self.calculator.total_expression = "10+5*2"
        self.calculator.evaluate()
        self.assertEqual(self.calculator.current_expression, "20")

if __name__ == "__main__":
    unittest.main()

