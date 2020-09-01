#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35a: gematria_dict"""

import string
import json


def gematria_dict():
    """Function that returns a dictionary of ASCII values
for all lowercase letters. The keys are the letters, and
the values are the numbers, starting with 1 for 'a'.
"""
    return {letter: number for number, letter in enumerate(string.ascii_lowercase, 1)}


def read_config():
    """
    Many programs’ functionality is modified via configuration files, which are often
    set using name-value pairs. That is, each line of the file contains text in the form
    of name=value, where the = sign separates the name from the value.
    I’ve prepared one such sample config file at http://mng.bz/rryD. Download this file,
    and then use a dict comprehension to read its contents from disk, turning it into
    a dict describing a user’s preferences. Note that all of the values will be strings.
    """
    with open('config.txt') as file:
        return {line.split('=')[0]: line.split('=')[1].strip() for line in file}


def read_config_integers():
    """
    Create a dict based on the config file, as in the previous exercise, but this time,
    all of the values should be integers. This means that you’ll need to filter out
    (and ignore) those values that can’t be turned into integers.
    """
    with open('config.txt') as file:
        return {line.split('=')[0]: int(line.split('=')[1].strip()) for line in file
                if line.split('=')[1].strip().isdigit()}


def read_json():
    """
    It’s sometimes useful to transform data from one format into another.
    Download a JSON-formatted list of the 1,000 largest cities in the United States from
    http://mng.bz/Vgd0. Using a dict comprehension, turn it into a dict in which
    the keys are the city names, and the values are the populations of those cities.
    Why are there only 925 key-value pairs in this dict? Now create a new dict, but
    set each key to be a tuple containing the state and city. Does that ensure there
    will be 1,000 key-value pairs?
    """
    with open('cities.json') as file:
        return {(one['city'], one['state']): one['population'] for one in json.load(file)}


# print(gematria_dict())
# print(read_config())
# print(read_config_integers())
# print(read_json())

