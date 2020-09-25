#!/usr/bin/env python3

"""Solution to chapter 9, exercise 40: limited size bowl"""


class Scoop:
    """Class representing a single scoop of ice cream.
    The sole attribute is "flavor", a string.
    """
    def __init__(self, flavour):
        self.flavour = flavour


def create_scoops():
    """Function that creates three scoops, puts them
    in a list, and iterates over that list, printing the
    flavors.
    """
    scoops = [Scoop(x) for x in ('chocolate', 'vanilla', 'persimmon')]

    for one in scoops:
        print(one.flavour)


class Bowl:
    """Class representing a bowl of ice cream.

    The class attribute max_scoops indicates the
    maximum number of scoops that the bowl can contain,
    assuming that the "add_scoops" method is used
    to add them.

    The "scoops" attribute is a list, containing scoops.
    You can add one or more scoops with the "add_scoops" method.
    """
    max_scoops = 3

    def __init__(self):
        self.scoops = []


    def add_scoops(self, *scoops):
        """
        adding scoops into the bowl
        """
        for one in scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one)


    def __repr__(self):
        return ', '.join(x.flavour for x in self.scoops)
