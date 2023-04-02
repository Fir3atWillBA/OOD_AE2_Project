import unittest
from tkinter import Tk
from calculator_code import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.root = Tk()
        self.app = Calculator(master=self.root)
        self.app.total_label = self.app.label = None # Remove label creation from constructor
        self.app.create_display_labels() # Create labels manually
        self.app.buttons_frame = self.app.create_buttons_frame()
        self.app.create_digit_buttons()
        self.app.create_operator_buttons()
        self.app.create_special_buttons()
        self.app.bind_keys()

    def test_smoke(self):
        self.app.add_to_expression(2)
        self.app.append_operator("+")
        self.app.add_to_expression(3)
        self.app.evaluate()
        self.assertEqual(self.app.current_expression, "5")

    def test_addition(self):
        self.app.add_to_expression(5)
        self.app.append_operator("+")
        self.app.add_to_expression(3)
        self.app.evaluate()
        self.assertEqual(self.app.current_expression, "8")

    def test_subtraction(self):
        self.app.add_to_expression(5)
        self.app.append_operator("-")
        self.app.add_to_expression(3)
        self.app.evaluate()
        self.assertEqual(self.app.current_expression, "2")

    def test_multiplication(self):
        self.app.add_to_expression(5)
        self.app.append_operator("*")
        self.app.add_to_expression(3)
        self.app.evaluate()
        self.assertEqual(self.app.current_expression, "15")

    def test_division(self):
        self.app.add_to_expression(10)
        self.app.append_operator("/")
        self.app.add_to_expression(2)
        self.app.evaluate()
        self.assertEqual(self.app.current_expression, "5")

    def test_clear(self):
        self.app.add_to_expression(10)
        self.app.clear()
        self.assertEqual(self.app.current_expression, "")
        self.assertEqual(self.app.total_expression, "")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
