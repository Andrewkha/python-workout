#!/usr/bin/env python3

"""Solution to chapter 7, exercise 32: flipped_dict"""


from pathlib import Path


def flipped_dict():
    """Gets a dict as an argument.
    Returns a dict as output. The output dict's keys
    are the input dict's values, and vice versa.
    """
    _dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    return {value: key for key, value in _dict.items()}


def vowels_dict(string):
    """Given a string containing several (space-separated) words, create a dict in which
    the keys are the words, and the values are the number of vowels in each word. If
    the string is “this is an easy test,” then the resulting dict would be {'this':1,
    'is':1, 'an':1, 'easy':2, 'test':1}"""

    def count_vowels(word):
        vowels = 'aeiou'
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count

    return {word: count_vowels(word) for word in string.split()}


def files():
    """
    Create a dict whose keys are filenames and whose values are the lengths of the
    files. The input can be a list of files from os.listdir (http://mng.bz/YreB) or
    glob.glob (http://mng.bz/044N).
    """
    return {file.name: file.stat().st_size for file in Path.cwd().iterdir() if file.is_file()}


# print(flipped_dict())
# print(vowels_dict('this is an easy test'))

print(files())

