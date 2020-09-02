#!/usr/bin/env python3

"""Solution to chapter 8, exercise 36: freedonia"""

RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}


def time_percentage(hour):
    """This function takes an integer from 0-24 and returns
the percentage of the day, as a float, that has passed at that hour.
"""
    return hour / 24


def calculate_tax(amount, state, hour):
    """This function returns the tax due in Freedonia based on the
original amount, the state, and the hour at which the purchase was
made. It returns the total amount, including the tax, that is due,
as a float.
"""

    return amount * (1 + RATES[state] * time_percentage(hour))


def char_type(string):
    """
    Write a module providing a function that, given a string, returns a dict indicating
    how many characters provide a True result to each of the following functions:
    str.isdigit, str.isalpha, and str.isspace. The keys should be isdigit,
    isalpha, and isspace.
    """
    result = {}
    funcs = (str.isdigit, str.isalpha, str.isspace)

    for char in string:
        for func in funcs:
            if func(char):
                result[func.__name__] = result.get(func.__name__, 0) + 1

    return result


def map_dicts(string, func):
    """
    The dict.fromkeys method (http://mng.bz/1zrV) makes it easy to create a
    new dict. For example, dict.fromkeys('abc') will create the dict {'a':None,
    'b':None, 'c':None}. You can also pass a value that will be assigned to each
    key, as in dict.fromkeys('abc', 5), resulting in the dict {'a':5, 'b':5,
    'c':5}. Implement a function that does the same thing as dict.keys but whose
    second argument is a function. The value associated with the key will be the
    result of invoking f(key)
    """
    return {char: func(char) for char in string}


print(char_type('hdfh23723   sd sd3484'))
print(map_dicts('asdwedfsd'))

