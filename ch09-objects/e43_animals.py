#!/usr/bin/env python3

"""Solution to chapter 9, exercise 43: animals"""


class Animal:
    """Base class for animals. Not meant to be instantiated."""
    legs = None

    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__

    def __repr__(self):
        return f"{self.color.capitalize()} {self.species}, {self.legs} legs"


class Wolf(Animal):
    """Class for creating 4-legged wolves of any color"""
    legs = 4


class Sheep(Animal):
    """Class for creating 4-legged sheep of any color"""
    legs = 4


class Snake(Animal):
    """Class for creating 0-legged snakes of any color"""
    legs = 0


class Parrot(Animal):
    """Class for creating 2-legged parrots of any color"""
    legs = 2

