"""This module provides access to class Rectangle."""

class Rectangle:
    """
    A class used to represent a rectangle.

    Args:
        a (int | float): The length of the rectangle.
        b (int | float): The width of the rectangle.

    Attributes:
        a (int | float): The length of the rectangle.
        b (int | float): The width of the rectangle.
    """

    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def square(self) -> int | float:
        """Returns the square of the rectangle."""

        return self.a * self.b

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __add__(self, other):
        """Return self+other"""

        if isinstance(other, Rectangle):
            return Rectangle(self.a, ((self.square() + other.square()) / self.a))
        if isinstance(other, int | float):
            return Rectangle(self.a, (self.square() + other) / self.a)
        return NotImplemented

    def __radd__(self, other):
        """Return other+self"""

        if isinstance(other, int | float):
            return Rectangle(self.a, (self.square() + other) / self.a)
        return NotImplemented

    def __mul__(self, other):
        """Return self*other"""

        if isinstance(other, int | float):
            return Rectangle((self.a * other), self.b)
        return NotImplemented

    def __rmul__(self, other):
        """Return other*self"""

        if isinstance(other, int | float):
            return Rectangle((self.a * other), self.b)
        return NotImplemented

    def __str__(self):
        return f"{self.a} x {self.b}"



