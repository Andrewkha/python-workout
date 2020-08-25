#!/usr/bin/env python3

"""Solution to chapter 6, exercise 27: makepw"""

import random
import string


def create_password_generator(characters):
    """This function takes a string as input.
    It returns a function that, when invoked with an
    integer argument, returns a string containing
    a random selection from "characters", of length
    "length".
    """
    def get_password(length):
        result = []
        for _ in range(length):
            result.append(random.choice(characters))
        return ''.join(result)

    return get_password


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    """
    Now that you’ve written a function to create passwords, write create_password_checker,
    which checks that a given password meets the IT staff’s acceptability criteria.
    In other words, create a function with four parameters: min_uppercase, min_lowercase,
    min_punctuation, and min_digits. These represent the minimum number of uppercase letters,
    lowercase letters, punctuations, and digits for an acceptable password.
    The output from create_password_checker is a function that takes a potential password (string)
    as its input and returns a Boolean value indicating whether the string is an acceptable password
    """

    def checker(password):
        chars = {}
        for one in password:
            if one in string.ascii_uppercase:
                chars['upper'] = chars.get('upper', 0) + 1
            if one in string.ascii_lowercase:
                chars['lower'] = chars.get('lower', 0) + 1
            if one in string.digits:
                chars['digits'] = chars.get('digits', 0) + 1
            if one in string.punctuation:
                chars['punctuation'] = chars.get('punctuation', 0) + 1

        return chars.get('upper', 0) >= min_uppercase and chars.get('lower', 0) >= min_lowercase and \
               chars.get('digits', 0) >= min_digits and chars.get('punctuation', 0) >= min_punctuation

    return checker


def getitem(arg):
    """
    Write a function, getitem, that takes a single argument and returns a function
    f. The returned f can then be invoked on any data structure whose elements
    can be selected via square brackets, and then returns that item. So if I invoke
    f = getitem('a'), and if I have a dict d = {'a':1, 'b':2}, then f(d) will return
    1. (This is very similar to operator.itemgetter, a very useful function in many
    circumstances.)
    """
    def f(sequence):
        return sequence[arg]

    return f


def do_both(f1, f2):
    """
    Write a function, doboth, that takes two functions as arguments (f1 and f2) and
    returns a single function, g. Invoking g(x) should return the same result as
    invoking f2(f1(x)).
    """
    def g(x):
        return f2(f1(x))

    return g


# alfa_password = create_password_generator('asdfghj')
# digit_password = create_password_generator('1234567890')
# print(alfa_password(10))
# print(digit_password(10))
# check = create_password_checker(1, 1, 1, 1)
# print(check('qw12A'))
a = getitem('a')
print(a({'s': 1, 'b': 3, 'a': 9}))
b = getitem(1)
print(b([1, 3, 2, 4, 5, 6]))

c = do_both(lambda x: x**2, lambda x: x + 5)
print(c(5))

