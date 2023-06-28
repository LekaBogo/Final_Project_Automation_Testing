import unittest
import math

# Definirea clasei Circle (Cerc)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# Definirea clasei Rectangle (Dreptunghi)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Definirea clasei Triangle (Triunghi)
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Formula lui Heron pentru calculul ariei triunghiului
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Definirea claselor de test
class TestCircle(unittest.TestCase):
    def test_area(self):
        # Test pentru metoda area() a clasei Circle
        circle = Circle(5)
        # Verificare: Aria cercului cu raza 5 ar trebui să fie aproximativ 78.5398
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=4)

    def test_circumference(self):
        # Test pentru metoda circumference() a clasei Circle
        circle = Circle(5)
        # Verificare: Circumferința cercului cu raza 5 ar trebui să fie aproximativ 31.4159
        self.assertAlmostEqual(circle.circumference(), 31.41592653589793, places=4)


class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test pentru metoda area() a clasei Rectangle
        rectangle = Rectangle(4, 6)
        # Verificare: Aria dreptunghiului cu lungimea 4 și lățimea 6 ar trebui să fie 24
        self.assertEqual(rectangle.area(), 24)

    def test_perimeter(self):
        # Test pentru metoda perimeter() a clasei Rectangle
        rectangle = Rectangle(4, 6)
        # Verificare: Perimetrul dreptunghiului cu lungimea 4 și lățimea 6 ar trebui să fie 20
        self.assertEqual(rectangle.perimeter(), 20)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        # Test pentru metoda area() a clasei Triangle
        triangle = Triangle(3, 4, 5)
        # Verificare: Aria triunghiului cu laturile 3, 4 și 5 ar trebui să fie 6.0
        self.assertEqual(triangle.area(), 6.0)

    def test_perimeter(self):
        # Test pentru metoda perimeter() a clasei Triangle
        triangle = Triangle(3, 4, 5)
        # Verificare: Perimetrul triunghiului cu laturile 3, 4 și 5 ar trebui să fie 12
        self.assertEqual(triangle.perimeter(), 12)


# Verificarea dacă scriptul este rulat ca fișier principal
if __name__ == '__main__':
    unittest.main()
