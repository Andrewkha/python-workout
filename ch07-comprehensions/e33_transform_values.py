#!/usr/bin/env python3

"""Solution to chapter 7, exercise 33: transform_values"""


def transform_values(func, a_dict):
    """Takes two arguments, a function and a dict.
    Returns a dict in which the keys are the original
    dict's keys, but the values are the result of invoking
    the function on each original value.
    """

    return {key: func(value) for key, value in a_dict.items()}


def transform_values_2(func1, func2, _dict):
    """
    Expand the transform_values exercise, taking two function arguments, rather
    than just one. The first function argument will work as before, being applied to
    the value and producing output. The second function argument takes two arguments,
    a key and a value, and determines whether there will be any output at
    all. That is, the second function will return True or False and will allow us to
    selectively create a key-value pair in the output dict
    """

    return {key: func1(value) for key, value in _dict.items() if func2(key, value)}


def lnx():
    """
     Use a dict comprehension to create a dict in which the keys are usernames and
    the values are (integer) user IDs, based on a Unix-style /etc/passwd file. Hint:
    in a typical /etc/passwd file, the usernames are the first field in a row (i.e.,
    index 0), and the user IDs are the third field in a row (i.e., index 2). If you need
    to download a sample /etc/passwd file, you can get it from http://mng.bz/
    2XXg. Note that this sample file contains comment lines, meaning that you’ll
    need to remove them when creating your dict.
    """
    with open('passwords.txt') as file:
        return {line.split(':')[0]: int(line.split(':')[3]) for line in file.readlines() if len(line.split(':')) > 1}


print(transform_values(lambda x: x*x, {'a': 1, 'b': 2, 'c': 3}))
print(lnx())
