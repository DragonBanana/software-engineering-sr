from abc import ABC, abstractmethod

# Abstract base class for GeometricShape
class GeometricShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class: Rectangle
class Rectangle(GeometricShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Concrete class: Square (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


# Concrete class: Triangle
class Triangle(GeometricShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Approximation: Assume an equilateral triangle
        return 3 * self.base


# Example usage
if __name__ == "__main__":
    # Create shapes
    rectangle = Rectangle(4, 6)
    square = Square(4)
    triangle = Triangle(5, 4)

    # Calculate and display areas and perimeters
    print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
    print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")
    print(f"Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")
