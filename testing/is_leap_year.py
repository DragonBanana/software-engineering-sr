def is_leap_year(year):
    """Determine if a given year is a leap year."""
    if not isinstance(year, int) or year <= 0:
        raise ValueError("Year must be a positive integer")

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

import unittest
# from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(is_leap_year(2020))  # Divisible by 4, not by 100
        self.assertFalse(is_leap_year(1900))  # Divisible by 4 and 100, not by 400
        self.assertTrue(is_leap_year(2000))  # Divisible by 4, 100, and 400
        self.assertFalse(is_leap_year(2021))  # Not divisible by 4

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            is_leap_year(-500)  # Negative year
        with self.assertRaises(ValueError):
            is_leap_year("2020")  # Non-integer input

if __name__ == "__main__":
    unittest.main()