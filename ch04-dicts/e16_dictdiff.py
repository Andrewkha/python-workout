#!/usr/bin/env python3
"""Solution to chapter 4, exercise 16: dictdiff"""


def dictdiff(first, second):
    """Accepts two dicts as arguments.
Returns a dict describing the differences between the two arguments.
Each key-value pair in the returned dict represents a difference. Each
difference consists of a key and a two-element list, indicating the
values from the two input dicts.  If a key exists in one dict but not
another, then the corresponding value will be None.
"""
