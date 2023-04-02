import unittest
from calculator_code import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate("5 + 3")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.calculate("5 - 3")
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.calculate("5 * 3")
        self.assertEqual(result, 15)

    def test_division(self):
        result = self.calculator.calculate("10 / 2")
        self.assertEqual(result, 5)

    def test_complex_expression(self):
        result = self.calculator.calculate("5 + 3 * 2 - 6 / 3")
        self.assertEqual(result, 10)

    def tearDown(self):
        del self.calculator

if __name__ == '__main__':
    unittest.main()
