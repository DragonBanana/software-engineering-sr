class Product:
    def __init__(self, name, price):
        self._name = name  # Private attribute (read-only)
        self._price = price  # Private attribute with getter and setter
        self._discount = 0   # Private attribute (write-only)

    # Read-only property for product name
    @property
    def name(self):
        return self._name

    # Getter for product price
    @property
    def price(self):
        return self._price

    # Setter for product price with validation
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be a positive value.")
        self._price = value

    # Write-only property for discount
    @property
    def discount(self):
        raise AttributeError("Discount is write-only.")

    @discount.setter
    def discount(self, percentage):
        if not (0 <= percentage <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        self._discount = percentage
        self.apply_discount()

    # Apply the discount to the price
    def apply_discount(self):
        self._price = self._price * (1 - self._discount / 100)

    # String representation of the product
    def __str__(self):
        return f"Product(name: {self.name}, price: ${self.price:.2f})"

# Example usage
if __name__ == "__main__":
    # Create a product
    product = Product("Laptop", 1000)
    print(product)  # Output: Product(name: Laptop, price: $1000.00)

    # Update the price
    product.price = 1200
    print(product)  # Output: Product(name: Laptop, price: $1200.00)

    # Apply a discount
    product.discount = 20
    print(product)  # Output: Product(name: Laptop, price: $960.00)

    # Attempt to read the discount (should raise an error)
    try:
        print(product.discount)
    except AttributeError as e:
        print(e)  # Output: Discount is write-only.

    # Attempt to set a negative price (should raise an error)
    try:
        product.price = -500
    except ValueError as e:
        print(e)  # Output: Price must be a positive value.
