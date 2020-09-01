#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49: elapsed_since"""

import time


def elapsed_since(data):
    """A generator that takes an iterable as input.

With each iteration, it yields a tuple containing the
data and the time since the previous iteration.
"""

