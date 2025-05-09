import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def description(self):
        return "This is a generic shape."

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def description(self):
        return f"This is a circle with radius {self.radius}."

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def description(self):
        return f"This is a rectangle with width {self.width} and height {self.height}."

# Derived class - Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def description(self):
        return f"This is a triangle with base {self.base} and height {self.height}."

# Test the classes
shapes = [
    Circle(radius=5),
    Rectangle(width=4, height=6),
    Triangle(base=3, height=7)
]

for shape in shapes:
    print(shape.description())
    print(f"Area: {shape.area():.2f}")
    print("-" * 30)
