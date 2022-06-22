#!/usr/bin/python3
"""
A module containing the square class task 2
"""


class Square:
    """
    A square class for the alx project
    """
    def __init__(self, size=0):
        """
        Initialize the class
        Args:
            size: The size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = 
