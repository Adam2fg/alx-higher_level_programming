#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is non-negative
        elif size < 0:
            raise ValueError("size must be >= 0")
        # Initialize size as a private instance attribute
        self.__size = size
