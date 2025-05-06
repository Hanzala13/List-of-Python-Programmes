import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius

# Example usage
if __name__ == "__main__":
    circle = Circle(5)  # Circle with radius 5
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")
