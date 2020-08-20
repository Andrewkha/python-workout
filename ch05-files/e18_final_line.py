#!/usr/bin/env python3
"""Solution to chapter 5, exercise 18: get_final_line"""


def get_final_line(filename):
    """Given a filename, returns the final line in that file."""
    # with open(filename) as file:
    #     text = file.readlines()
    #
    # return text[-1]
    final_line = ''

    for line in open(filename):
        final_line = line

    return final_line


def get_integers_file():
    """
    Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
    surrounded by whitespace) that contain only integers, and sum them
    """
    result = 0
    for line in open('shoe-data.txt'):
        for one in line.split():
            try:
                result += int(one)
            except ValueError:
                continue

    return result


def two_columns_of_numbers():
    """
    Create a text file (using an editor, not necessarily Python) containing two tabseparated columns,
    with each column containing a number. Then use Python to read through the file you’ve created.
    For each line, multiply each first number by the second, and then sum the results from all the lines.
    Ignore any linenums.txt that doesn’t contain two numeric columns
    """
    result = 0
    for line in open('nums1.txt'):
        try:
            one, two = line.split()[0], line.split()[1]
            result += int(one) * int(two)
        except IndexError:
            continue

    return result


def count_vowels():
    """
    Read through a text file, line by line. Use a dict to keep track of how many times
    each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
    """
    vowels = 'aioue'
    result = {}

    for char in open('shoe-data.txt').read():
        if char.lower() in vowels:
            result[char.lower()] = result.get(char.lower(), 0) + 1

    return result


print(get_final_line('shoe-data.txt'))
print(get_integers_file())
print(two_columns_of_numbers())
print(count_vowels())
