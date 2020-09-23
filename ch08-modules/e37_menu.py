#!/usr/bin/env python3

"""Solution to chapter 8, exercise 37: menu"""


def menu(**options):
    """Function that takes keyword arguments. The value
    associated with each key is a function taking zero arguments.

    The user is asked to enter input.

    If the input matches a keyword, then the associated function
    is invoked, and its return value is returned to the user.

    If the input doesn't match a keywork, the user is asked to
    try again.
    """

    while True:
        user_input = input('Please provide the function to invoke: ')
        if user_input in options:
            return options[user_input]()

        print('Wrong option, try again')


def func_a():
    return "A"


def func_b():
    return "B"


if __name__ == '__main__':
    return_value = menu(a=func_a, b=func_b)
    print(f'Result is {return_value}')
