#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9: firstlast"""


def firstlast(sequence):
    """Given a sequence, returns a two-element sequence.
The returned sequence will be of the same type as the argument.
Its two elements will be the argument's first and last elements.
"""
    # return sequence[0::len(sequence) - 1]
    return sequence[:1] + sequence[-1:]


def even_odd_summ(sequence):
    """Write a function that takes a list or tuple of numbers. Return a two-element list,
    containing (respectively) the sum of the even-indexed numbers and the sum of
    the odd-indexed numbers. So calling the function as even_odd_sums([10, 20,
    30, 40, 50, 60]), you’ll get back [90, 120]."""

    return [sum(sequence[0::2]), sum(sequence[1::2])]


def add_substract(sequence):
    """Write a function that takes a list or tuple of numbers. Return the result of alternately
    adding and subtracting numbers from each other. So calling the function as
    plus_minus([10, 20, 30, 40, 50, 60]), you’ll get back the result of 10+20-30+40-50+60, or 50
    """

    return sequence[0] + sum(sequence[1::2]) - sum(sequence[2::2])


def aka_zip(*sequences):
    """Write a function that partly emulates the built-in zip function (http://mng.bz/
    Jyzv), taking any number of iterables and returning a list of tuples. Each tuple
    will contain one element from each of the iterables passed to the function.
    Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20,
    'b'), (30, 'c')]. You can return a list (not an iterator) and can assume that all
    of the iterables are of the same length"""

    result = []
    length = len(sequences[0]) if len(sequences) > 0 else 0

    for i in range(0, length):
        result.append(tuple(x[i] for x in sequences))

    return result


print(firstlast('absdasdsdce'))
print(even_odd_summ([10, 20, 30, 40, 50, 60]))
print(add_substract([10, 20, 30, 40, 50, 60]))
print(aka_zip([10, 20, 30], 'abc'))
print(aka_zip())
