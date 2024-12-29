class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_items(self):
        return self.items

import unittest
# from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Laptop", 1000, 2)
        self.assertEqual(self.cart.get_items()["Laptop"]["quantity"], 2)
        self.assertEqual(self.cart.get_items()["Laptop"]["price"], 1000)

    def test_remove_item(self):
        self.cart.add_item("Laptop", 1000, 1)
        self.cart.remove_item("Laptop")
        self.assertNotIn("Laptop", self.cart.get_items())

    def test_get_total_price(self):
        self.cart.add_item("Laptop", 1000, 2)
        self.cart.add_item("Mouse", 50, 1)
        self.assertEqual(self.cart.get_total_price(), 2050)

if __name__ == "__main__":
    unittest.main()


class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount = 0  # New attribute for discounts

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def set_discount(self, percentage):
        """Set a discount as a percentage."""
        if not (0 <= percentage <= 100):
            raise ValueError("Discount must be between 0 and 100")
        self.discount = percentage

    def get_total_price(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total * (1 - self.discount / 100)

    def get_items(self):
        return self.items

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    # Existing tests
    def test_add_item(self):
        self.cart.add_item("Laptop", 1000, 2)
        self.assertEqual(self.cart.get_items()["Laptop"]["quantity"], 2)
        self.assertEqual(self.cart.get_items()["Laptop"]["price"], 1000)

    def test_remove_item(self):
        self.cart.add_item("Laptop", 1000, 1)
        self.cart.remove_item("Laptop")
        self.assertNotIn("Laptop", self.cart.get_items())

    def test_get_total_price(self):
        self.cart.add_item("Laptop", 1000, 2)
        self.cart.add_item("Mouse", 50, 1)
        self.assertEqual(self.cart.get_total_price(), 2050)

    # New test for discount feature
    def test_set_discount(self):
        self.cart.add_item("Laptop", 1000, 2)
        self.cart.add_item("Mouse", 50, 1)
        self.cart.set_discount(10)  # 10% discount
        self.assertEqual(self.cart.get_total_price(), 1845)  # 2050 - 10%

    # Test invalid discount value
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.cart.set_discount(-5)  # Invalid discount
        with self.assertRaises(ValueError):
            self.cart.set_discount(105)  # Invalid discount

if __name__ == "__main__":
    unittest.main()