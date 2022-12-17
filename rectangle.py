"""This module provides access to class `Rectangle`."""

class Rectangle:
    """
    A class used to represent a rectangle.

    Args:
        a (int): The length of the rectangle.
        b (int): The width of the rectangle.

    Attributes:
        a (int): The length of the rectangle.
        b (int): The width of the rectangle.

    Methods:
        square(a, b):
            Returns the square of the rectangle.

    """

    def __init__(self, a: int, b: int):


        self.a = a
        self.b = b

    def __str__(self):

        return f"{self.a} x {self.b}"



