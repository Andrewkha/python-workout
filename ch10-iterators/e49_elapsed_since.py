#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49: elapsed_since"""

import time


def elapsed_since(data):
    """A generator that takes an iterable as input.
    With each iteration, it yields a tuple containing the
    data and the time since the previous iteration.
    """

    last_time = None

    for item in data:
        curr_time = time.perf_counter()
        delta = curr_time - (last_time or curr_time)
        last_time = time.perf_counter()
        yield item, delta


def iter_func(iterable, func):
    """Write a generator function that takes two elements: an iterable and a function.
    With each iteration, the function is invoked on the current element. If the
    result is True, then the element is returned as is. Otherwise, the next element is
    tested, until the function returns True. Alternative: implement this as a regular
    function that returns a generator expression"""

    for element in iterable:
        if func(element):
            yield element


def iter_func_expr(iterable, func):
    """
    Alternative: implement this as a regular
    function that returns a generator expression
    """

    return (element for element in iterable if func(element))

#
# for one in elapsed_since('jrtyip'):
#     print(one)


for one in iter_func_expr('AsWedERT', str.isupper):
    print(one)

for one in iter_func('AsWedERT', str.isupper):
    print(one)
