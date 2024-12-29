def is_palindromic_number(n):
    """Check if the given number is a palindromic number."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        return False

    str_n = str(n)
    return str_n == str_n[::-1]

import unittest
# from palindrome_number import is_palindromic_number

class TestIsPalindromicNumber(unittest.TestCase):
    def test_palindromic_number(self):
        self.assertTrue(is_palindromic_number(121))  # Palindromic number
        self.assertFalse(is_palindromic_number(123))  # Non-palindromic number

    def test_negative_number(self):
        self.assertFalse(is_palindromic_number(-121))  # Negative input

    def test_single_digit_number(self):
        self.assertTrue(is_palindromic_number(0))  # Single-digit number

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_palindromic_number("121")  # Non-integer input

if __name__ == "__main__":
    unittest.main()