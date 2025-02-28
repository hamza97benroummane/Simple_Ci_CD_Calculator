
import unittest
from unittest.mock import patch
from MyCode import get_user_input, calculate_sum  # Import functions
# import MyCode

class TestCalculator(unittest.TestCase):

    def test_calculate_sum(self):
        """Test the sum function with different inputs."""
        self.assertEqual(calculate_sum(3, 5), 8)
        self.assertEqual(calculate_sum(-2, 2), 0)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1.5, 2.5), 4.0)

    @patch('builtins.input', side_effect=["3", "5"])
    def test_get_user_input(self, mock_input):
        """Test the user input function by mocking input."""
        a, b = get_user_input()
        self.assertEqual(a, 3.0)
        self.assertEqual(b, 5.0)

if __name__ == "__main__":
    unittest.main()
