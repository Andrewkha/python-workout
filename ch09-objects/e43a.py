"""
Instead of each animal class inheriting directly, from Animal, define several new
classes, ZeroLeggedAnimal, TwoLeggedAnimal, and FourLeggedAnimal, all of
which inherit from Animal, and dictate the number of legs on each instance.
Now modify Wolf, Sheep, Snake, and Parrot such that each class inherits from
one of these new classes, rather than directly from Animal. How does this affect
your method definitions?
"""


class Animal:
    """Base class for animals. Not meant to be instantiated."""
    legs = None
    voice = None
    space_required = None
    coexists = None

    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__

    def __repr__(self):
        return f"{self.voice} - {self.color.capitalize()} {self.species}, {self.legs} legs"


class ZeroLeggedAnimal(Animal):
    """Zero legged animals"""
    legs = 0


class TwoLeggedAnimal(Animal):
    """Two legged animals"""
    legs = 2


class FourLeggedAnimal(Animal):
    """Four legged animals"""
    legs = 4


class Wolf(FourLeggedAnimal):
    """Class for creating 4-legged wolves of any color"""
    voice = 'Woooo'
    space_required = 2
    coexists = {'Snake', 'Parrot', 'Wolf'}


class Sheep(FourLeggedAnimal):
    """Class for creating 4-legged sheep of any color"""
    voice = 'Bee'
    space_required = 2
    coexists = {'Snake', 'Parrot', 'Sheep'}


class Snake(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""
    voice = 'Shhheee'
    space_required = 1
    coexists = {'Wolf', 'Sheep', 'Snake'}


class Parrot(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""
    voice = 'Kar'
    space_required = 1
    coexists = {'Wolf', 'Sheep', 'Parrot'}


if __name__ == "__main__":
    sheep = Sheep('white')
    print(sheep)
