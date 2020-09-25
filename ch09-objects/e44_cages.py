#!/usr/bin/env python3

"""Solution to chapter 9, exercise 44: cages"""

from e43a import *


class TooManyAnimalsException(Exception):
    """exception to raise when not enough space in the cage"""
    pass


class CoexistanceException(Exception):
    """exception to raise when co-existance issue occurs"""
    pass


"""
Our zookeepers have a macabre sense of humor when it comes to placing animals together, 
in that they put wolves and sheep in the first cage, and snakes
and birds in the other cage. (The good news is that with such a configuration,
the zoo will be able to save on food for half of the animals.) Define a dict
describing which animals can be with others. The keys in the dict will be classes,
and the values will be lists of classes that can compatibly be housed with the
keys. Then, when adding new animals to the current cage, you’ll check for compatibility. 
Trying to add an animal to a cage that already contains an incompatible animal will raise an exception.
"""


class Cage:
    """Class for creating cages in which to put cute, furry animals."""

    space = 2

    def __init__(self, id_number):
        self.id = id_number
        self.animals = []
        self.space_occupied = 0

    def add_animals(self, *animals):
        """Add one or more animals to a cage.  Returns None."""

        for one in animals:

            in_cage = {animal.__class__.__name__ for animal in self.animals}
            total = in_cage.union(one.coexists)
            if total == one.coexists:
                if one.space_required + self.space_occupied <= self.space:
                    self.animals.append(one)
                    self.space_occupied += one.space_required
                else:
                    raise TooManyAnimalsException
            else:
                raise CoexistanceException

    def __repr__(self):
        animals = ", ".join(str(animal) for animal in self.animals)
        return f"The cage {self.id} has the following animals {animals}"


class BigCage(Cage):
    """Implements big cage"""
    space = 5


snake = Snake('blue')
sheep = Sheep('black')
wolf = Wolf('grey')

cage1 = BigCage(1)
cage1.add_animals(snake, sheep, wolf)

print(cage1)
