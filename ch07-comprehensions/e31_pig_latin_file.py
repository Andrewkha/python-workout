#!/usr/bin/env python3

import operator


"""Solution to chapter 7, exercise 31: plfile"""


def plword(word):
    """Takes a string as input. It should be a single
word.  Returns a string, the input word translated into
Pig Latin.
"""
    if word[0] in 'aeuio':
        return word + 'way'

    return word[1:] + word[0] + 'ay'


def plfile(filename):
    """Takes a filename as input. Returns a string
    containing the file's contents, with each word
    translated into Pig Latin.
    """

    with open(filename) as file:
        text = file.read()

    return ' '.join((plword(word) for word in text.split()))


def funcfile(filename, func):
    """
    In this exercise, plfile applied the plword function to every word in a file.
    Write a new function, funcfile, that will take two arguments—a filename and a
    function. The output from the function should be a string, the result of invoking
    the function on each word in the text file. You can think of this as a generic
    version of plfile, one that can return any string value.
    """
    with open(filename) as file:
        text = file.read()

    return ' '.join((func(word) for word in text.split()))


def dict_to_tuples():
    """
    Use a nested list comprehension to transform a list of dicts into a list of two element (name-value)
    tuples, each of which represents one of the name-value
    pairs in one of the dicts. If more than one dict has the same name-value pair,
    then the tuple should appear twice.
    """

    _list = [{'one': 1, 'two': 2, 'three': 3, 'four': 4},
             {'two': 2, 'five': 5},
             {'three': 3},
             {'six': 6, 'seven': 7}]

    return [(key, value) for item in _list for key, value in item.items()]


def hobbies():
    """
    Assume that you have a list of dicts, in which each dict contains two name-value
    pairs: name and hobbies, where name is the person’s name and hobbies is a set
    of strings representing the person’s hobbies. What are the three most popular
    hobbies among the people listed in the dicts?
    """
    _list = [{'name': 'Andrew', 'hobbies': {'guitar', 'beer', 'vodka', 'programming'}},
             {'name': 'Miha', 'hobbies': {'beer', 'vodka'}},
             {'name': 'Alexey', 'hobbies': {'dacha', 'beer', 'vodka', 'cars'}},
             {'name': 'Sanya', 'hobbies': {'cars', 'beer', 'traktor'}},
             {'name': 'Alex Nik', 'hobbies': {'guitar', 'beer', 'vodka', 'garmoshka', 'cars'}}]

    _hobbies = [hobbie for element in _list for hobbie in element['hobbies']]
    res = {one: _hobbies.count(one) for one in set(_hobbies)}
    return sorted(res, key=res.get, reverse=True)[0:3]

# print(plfile('shoe-data.txt'))
# print(funcfile('shoe-data.txt', str.upper))
# print(dict_to_tuples())
print(hobbies())
