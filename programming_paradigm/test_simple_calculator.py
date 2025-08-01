import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):  # This method is called before each test
        """Set up a Simple Calculator instance for testing."""
        self.calculator = SimpleCalculator()

        # addition tests
    def test_addition_positive_numbers(self):
        """Test addition of two positive numbers."""
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        """Test addition of two negative numbers."""
        result = self.calculator.add(-5, -3)
        self.assertEqual(result, -8)

    def test_addition_mixed_numbers(self):
        """Test addition of a positive and a negative number."""
        result = self.calculator.add(5, -3)
        self.assertEqual(result, 2)

    def test_addition_zero(self):
        """Test addition of zero to a number."""
        result = self.calculator.add(0, 5)
        self.assertEqual(result, 5)

    def test_addition_zero_to_zero(self):
        """Test addition of zero to zero."""
        result = self.calculator.add(0, 0)
        self.assertEqual(result, 0)

    # subtraction tests
    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_negative_numbers(self):
        """Test subtraction of two negative numbers."""
        result = self.calculator.subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_subtract_mixed_numbers(self):
        """Test subtraction of a positive and a negative number."""
        result = self.calculator.subtract(5, -3)
        self.assertEqual(result, 8)

    def test_subtract_zero(self):
        """Test subtraction of zero from a number."""
        result = self.calculator.subtract(5, 0)
        self.assertEqual(result, 5)

    def test_subtract_zero_from_zero(self):
        """Test subtraction of zero from zero."""
        result = self.calculator.subtract(0, 0)
        self.assertEqual(result, 0)

    # multiplication tests
    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        result = self.calculator.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_multiply_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        result = self.calculator.multiply(-5, -3)
        self.assertEqual(result, 15)

    def test_multiply_mixed_numbers(self):
        """Test multiplication of a positive and a negative number."""
        result = self.calculator.multiply(5, -3)
        self.assertEqual(result, -15)

    def test_multiply_zero(self):
        """Test multiplication of zero with a number."""
        result = self.calculator.multiply(5, 0)
        self.assertEqual(result, 0)

    def test_multiply_zero_with_zero(self):
        """Test multiplication of zero with zero."""
        result = self.calculator.multiply(0, 0)
        self.assertEqual(result, 0)
