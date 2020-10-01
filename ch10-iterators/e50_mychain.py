#!/usr/bin/env python3

"""Solution to chapter 10, exercise 50: mychain"""

from pathlib import Path

def mychain(*args):
    """Generator that takes any number of iterables
    as arguments. It yields, one at a time, each of the
    elements of each iterable.
    It is similar to itertools.chain.
    """
    for iterable in args:
        for element in iterable:
            yield element


# for one in mychain('adssf', [1, 2, 3, 4], {'d': 2, 5: 's'}):
#     print(one)

def my_zip(*args):
    """
    The built-in zip function returns an iterator that, given iterable arguments,
    returns tuples taken from those arguments’ elements. The first iteration will
    return a tuple from the arguments’ index 0, the second iteration will return a
    tuple from the arguments’ index 1, and so on, stopping when the shortest of
    the arguments ends. Thus zip('abc', [10, 20, 30]) returns the iterator
    equivalent of [('a', 10), ('b', 20), ('c', 30)]. Write a generator function that
    reimplements zip in this way
    """

    min_len = min(len(elem) for elem in args)

    for i in range(min_len):
        yield tuple(elem[i] for elem in args)


def all_lines(path):
    """Reimplement the all_lines function from exercise 49 using mychain
    An iterator that returns, one at a time, each line
    from each file in a named directory.
    Any file that cannot be opened, for whatever reason, is ignored.
    """

    pth = Path(path)

    files = [open(file) for file in pth.iterdir() if file.is_file()]
    return mychain(*files)


# print(list(all_lines('../ch08-modules')))


def my_range(start, end, step):
    """
     In the “Beyond the exercise” section for exercise 48, you implemented a MyRange
    class, which mimics the built-in range class. Now do the same thing, but using a
    generator expression
    """
    current = start

    while current < end:
        yield current
        current += step


for one in my_range(5, 10, 3):
    print(one)

