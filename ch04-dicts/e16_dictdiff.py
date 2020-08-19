#!/usr/bin/env python3
"""Solution to chapter 4, exercise 16: dictdiff"""

from collections.abc import Hashable

def dictdiff(first: dict, second: dict) -> dict:
    """Accepts two dicts as arguments.
    Returns a dict describing the differences between the two arguments.
    Each key-value pair in the returned dict represents a difference. Each
    difference consists of a key and a two-element list, indicating the
    values from the two input dicts.  If a key exists in one dict but not
    another, then the corresponding value will be None.
    """
    result = {}

    for key, value in first.items():
        if key not in second:
            result[key] = [value, None]
        else:
            if first[key] == second[key]:
                continue
            else:
                result[key] = [value, second[key]]

    for key, value in second.items():
        if key not in first:
            result[key] = [None, value]

    return result


def dictdiff_refactor(first: dict, second: dict) -> dict:
    """Accepts two dicts as arguments.
    Returns a dict describing the differences between the two arguments.
    Each key-value pair in the returned dict represents a difference. Each
    difference consists of a key and a two-element list, indicating the
    values from the two input dicts.  If a key exists in one dict but not
    another, then the corresponding value will be None.
    """
    result = {}

    for key, value in first.items():
        if first.get(key) == second.get(key):
            continue
        result[key] = [value, second.get(key)]

    for key, value in second.items():
        if key not in first:
            result[key] = [first.get(key), value]

    return result


def dictdiff_optimize(first: dict, second: dict) -> dict:
    """Accepts two dicts as arguments.
    Returns a dict describing the differences between the two arguments.
    Each key-value pair in the returned dict represents a difference. Each
    difference consists of a key and a two-element list, indicating the
    values from the two input dicts.  If a key exists in one dict but not
    another, then the corresponding value will be None.
    """
    result = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) == second.get(key):
            continue
        result[key] = [first.get(key), second.get(key)]

    return result


def merge_dicts(*dicts):
    """
    The dict.update method merges two dicts. Write a function that takes any
    number of dicts and returns a dict that reflects the combination of all of them.
    If the same key appears in more than one dict, then the most recently merged
    dict’s value should appear in the output
    """
    result = {}
    for one in dicts:
        result.update(one)

    return result


def create_dict(*args):
    """
    Write a function that takes any even number of arguments and returns a dict
    based on them. The even-indexed arguments become the dict keys, while the
    odd-numbered arguments become the dict values. Thus, calling the function
    with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being
    returned.
    """
    result = {}
    if len(args) % 2 != 0:
        print("Wrong number of args provided")

    for position in range(0, len(args), 2):
        if isinstance(args[position], Hashable):
            result[args[position]] = args[position + 1]
        else:
            continue

    return result


def partition(_dct: dict, func):
    """
    Write a function , dict_partition, that takes one dict (d) and a function (f) as
    arguments. dict_partition will return two dicts, each containing key-value
    pairs from d. The decision regarding where to put each of the key-value pairs
    will be made according to the output from f, which will be run on each keyvalue pair in d.
    If f returns True, then the key-value pair will be put in the first
    output dict. If f returns False, then the key-value pair will be put in the second
    output dict
    """
    dict1 = {}
    dict2 = {}

    for key, value in _dct.items():
        if func(key, value):
            dict1[key] = value
        else:
            dict2[key] = value

    return dict1, dict2


# print(dictdiff_optimize({'a':1, 'b':2, 'c':3}, {'a':1, 'b':2, 'c':3}))
# print(dictdiff_optimize({'a':1, 'b':2, 'd':3}, {'a':1, 'b':2, 'c':4}))
# print(dictdiff_optimize({'a':1, 'b':2, 'c':3}, {'a':1, 'b':2, 'd':4}))

# print(merge_dicts({'a':1, 'b':2, 'c':3}, {'a':1, 'b':2, 'd':3}, {'a':1, 'b':2, 'c':4}, {'a':1, 'b':2, 'd':4}))
# print(create_dict(1, '2', 3, [1, 34, 5], ['d', 'da'], 4))
print(partition({1: 2, 2: 1, 10: 5, 5: 10}, lambda x, y: x > y))
