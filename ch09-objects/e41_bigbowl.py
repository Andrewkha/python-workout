#!/usr/bin/env python3

"""Solution to chapter 9, exercise 41: big bowl"""

from e40_limited_size_bowl import Scoop, Bowl


class BigBowl(Bowl):
    """Class representing a bigger bowl of ice cream."""
    max_scoops = 5
