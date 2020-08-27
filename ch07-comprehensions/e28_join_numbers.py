#!/usr/bin/env python3

"""Solution to chapter 7, exercise 28: join_numbers"""


def join_numbers(numbers):
    """Takes an iterable of numbers as input.
    Output is a string containing the numbers in that iterable,
    separated by commas.
    """
    return ','.join(str(x) for x in numbers)


def join_filtered_numbers(numbers):
    """
    As in the exercise, take a list of integers and turn them into strings. However,
    you’ll only want to produce strings for integers between 0 and 10. Doing this
    will require understanding the if statement in list comprehensions as well
    """

    return ','.join(str(x) for x in numbers if x < 11)


def hexidemical(_list):
    """
    Given a list of strings containing hexadecimal numbers, sum the numbers
    together.
    """
    return sum(int(x, 16) for x in _list)


def reverse(file):
    """
    Use a list comprehension to reverse the word order of lines in a text file. That
    is, if the first line is abc def and the second line is ghi jkl, then you should
    return the list ['def abc', 'jkl ghi']
    """
    with open(file) as f:
        text = f.readlines()

    with open('output.txt', 'w') as f:
        f.writelines(x[::-1] for x in text)


print(join_numbers(range(15)))
print(join_filtered_numbers(range(15)))
reverse('shoe-data.txt')
