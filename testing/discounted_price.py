def find_discounted_price(price, discount_code):
    """Calculate the discounted price based on the discount code."""
    if price <= 0:
        return "Invalid price"

    if discount_code == "DISCOUNT10":
        price *= 0.9  # Apply 10% discount
    elif discount_code == "DISCOUNT20":
        price *= 0.8  # Apply 20% discount
    elif discount_code == "DISCOUNT50":
        price *= 0.5  # Apply 50% discount
    else:
        return "Invalid discount code"

    if price < 1:
        return "Discount too large"

    return round(price, 2)

import unittest
# from discount import find_discounted_price

class TestDiscountedPrice(unittest.TestCase):
    def test_valid_discount(self):
        self.assertEqual(find_discounted_price(100, "DISCOUNT10"), 90.0)
        self.assertEqual(find_discounted_price(100, "DISCOUNT20"), 80.0)
        self.assertEqual(find_discounted_price(100, "DISCOUNT50"), 50.0)

    def test_invalid_discount_code(self):
        self.assertEqual(find_discounted_price(100, "INVALID"), "Invalid discount code")

    def test_invalid_price(self):
        self.assertEqual(find_discounted_price(-50, "DISCOUNT10"), "Invalid price")

    def test_discount_too_large(self):
        self.assertEqual(find_discounted_price(0.5, "DISCOUNT50"), "Discount too large")

# if __name__ == "__main__":
#     unittest.main()