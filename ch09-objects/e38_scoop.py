#!/usr/bin/env python3

"""Solution to chapter 9, exercise 38: scoop"""


class Scoop():
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


create_scoops()


"""
Create a new LogFile class that expects to be initialized with a filename.
Inside of __init__, open the file for writing and assign it to an attribute,
file, that sits on the instance. Check that it’s possible to write to the file via
the file attribute.
"""

class LogFile:
    def __init__(self, filename):
        self.file = open(filename, 'w')


logfile = LogFile('log.txt')
logfile.file.write('rrrrr')
logfile.file.close()
