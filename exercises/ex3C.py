class Shape:
    def set_width(self, width):
        pass

    def set_height(self, height):
        pass

    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height


def process_rectangle(rect):
    rect.set_width(5)
    rect.set_height(10)
    assert rect.get_area() == 50  # This assertion fails for Square

# Using a Rectangle
rect = Rectangle()
process_rectangle(rect)  # Works as expected

# Using a Square
square = Square()
process_rectangle(square)  # Fails, as the area is 100 instead of 50
