import unittest
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=4)

    def test_circumference(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.circumference(), 31.41592653589793, places=4)


class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.area(), 24)

    def test_perimeter(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.perimeter(), 20)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6.0)

    def test_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)


if __name__ == '__main__':
    unittest.main()
