#!/usr/bin/env python3
"""Solution to chapter 3, exercise 11: alphabetize_names"""

import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Valdemar', 'last': 'Putin',
           'email': 'president@kremvax.ru'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'},
          {'first': 'Voldemar', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]


def alphabetize_names(list_of_dicts):
    """Take a list of dicts describing people,
    each with first/last/email as keys.

    Return a new list of dicts,
    sorted first by last name and then by first name.

    If passed an empty list, then return an empty list.
    """
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


def sort_abs(sequence):
    """Given a sequence of positive and negative numbers, sort them by absolute value"""
    return sorted(sequence, key=abs)


def sort_vowels(list_of_strings):
    """Given a list of strings, sort them according to how many vowels they contain."""

    return sorted(list_of_strings, key=lambda _str: _str.count('a') + _str.count('e') + _str.count('u') +
                                                    _str.count('i') + _str.count('o'))


def sort_sum(list_of_ints):
    """Given a list of lists, with each list containing zero or more numbers, sort by the
    sum of each inner list’s numbers."""
    return sorted(list_of_ints, key=sum)


print(alphabetize_names(PEOPLE))
print(sort_abs([-1000, 300, -1, -10, 100, -200, -400]))
print(sort_vowels(['aaaaaaaa', 'ssddfoie', 'poevjkiea']))
print(sort_sum([[100, 105], [0], [1, 2, 3]]))

