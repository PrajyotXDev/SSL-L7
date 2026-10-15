import unittest
from calculator import add, subtract, multiply, divide, square

class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
    def test_subtract(self):
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(0, 0), 0)
    def test_multiply(self):
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 10), 0)
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-9, 3), -3)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
    def test_validation(self):
        with self.assertRaises(TypeError):
            add("1", 2)
if __name__ == "__main__":
    unittest.main()
