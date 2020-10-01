#!/usr/bin/env python3

"""Solution to chapter 9, exercise 45: zoo"""

from e44_cages import *


class InvalidArgument(Exception):
    pass


class Zoo:
    """A class in which to place our animals."""

    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        """Add one or more cages to our zoo"""
        for one in cages:
            self.cages.append(one)

    def __repr__(self):
        return '\n\n'.join(str(cage) for cage in self.cages)

    def animals_by_color(self, *colors):
        """Return a list of Animal objects whose
        color matches the requested color"""
        animals = []
        if not colors:
            raise Exception
        for color in colors:
            animals.extend([animal for cage in self.cages for animal in cage.animals if animal.color == color])

        return animals

    def animals_by_legs(self, number_of_legs):
        """Return a list of Animal objects whose
        number of legs matches the requested number"""
        return [animal for cage in self.cages for animal in cage.animals if animal.legs == number_of_legs]

    def number_of_legs(self):
        """Return the total number of legs of all animals"""
        return sum(animal.legs for cage in self.cages for animal in cage.animals)

    def animal_by_color_legs(self, **kwargs):
        """Combine the animals_by_color and animals_by_legs methods into a single
        get_animals method, which uses kwargs to get names and values. The only
        valid names would be color and legs. The method would then use one or both
        of these keywords to assemble a query that returns those animals that match the
        passed criteria"""
        for one in kwargs:
            if one not in ('color', 'legs'):
                raise InvalidArgument

        color = kwargs.get('color', None)
        legs = kwargs.get('legs', None)

        if color is not None and legs is not None:
            return [animal for cage in self.cages for animal in cage.animals
                    if animal.legs == legs and animal.color == color]

        if color and legs is None:
            return [animal for cage in self.cages for animal in cage.animals
                    if animal.color == color]

        if legs and color is None:
            return [animal for cage in self.cages for animal in cage.animals
                    if animal.legs == legs]

    def transfer_animal(self, target_zoo, animal: Animal):
        """Implement a Zoo.transfer_animal method that takes a target_zoo and a subclass of Animal
        as arguments. The first animal of the specified type is removed from the zoo on which we’ve
        called the method and inserted into the first cage in the target zoo."""
        if not target_zoo.cages:
            raise NoCagesInZooException
        for cage in self.cages:
            animal_to_transfer = cage.remove_animal(animal)
            if animal_to_transfer:
                target_zoo.cages[0].add_animals(animal_to_transfer)
                break


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('white')
snake2 = Snake('grey')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, parrot)

c2 = Cage(2)
c2.add_animals(snake, sheep)


c3 = Cage(3)

z1 = Zoo()
z1.add_cages(c1, c2)

z2 = Zoo()
z2.add_cages(c3)

print(z1.animal_by_color_legs(color='white', legs=0))

