#!/usr/bin/env python3
"""Solution to chapter 5, exercise 20: wc"""

import operator
from pathlib import Path
from string import ascii_lowercase


def wordcount(filename):
    """Accepts a filename as an argument. Prints the number of lines,
    characters, words (separated by whitespace) and different words
    (case sensitive) in the file."""
    result = {'chars': 0, 'words': 0, 'lines': 0, 'unique_words': 0}
    unique = set()

    with open(filename) as file:
        for line in file.readlines():
            result['lines'] += 1
            result['chars'] += len(line)
            result['words'] += len(line.split())
            unique.update(line.split())

    result['unique_words'] = len(unique)

    return result


def count_word():
    """Ask the user to enter the name of a text file and then (on one line, separated by
    spaces) words whose frequencies should be counted in that file. Count how
    many times those words appear in a dict, using the user-entered words as the
    keys and the counts as the values."""
    user_input = input('Provide a name of a file and words to search separated by space: ')
    text_file, *search_words = user_input.split()
    result = {}

    try:
        with open(text_file) as file:
            text = file.read()

    except FileNotFoundError:
        print('File doesn\'t exist')
        exit()

    for one in search_words:
        result[one] = text.count(one)

    return result


def files_size():
    """
    Create a dict in which the keys are the names of files on your system and the
    values are the sizes of those files. To calculate the size, you can use os.stat
    """
    result = {}
    files = Path.cwd().iterdir()
    for one in files:
        if one.is_file():
            result[one.name] = one.stat().st_size

    return result


def letter_frequency():
    """
    Given a directory, read through each file and count the frequency of each letter.
    (Force letters to be lowercase, and ignore nonletter characters.) Use a dict
    to keep track of the letter frequencies. What are the five most common letters
    across all of these files?
    """
    result = {}
    files = Path('..\\files').iterdir()

    for one in files:
        with open(one, encoding='utf-8') as file:
            text = file.read().lower()
            for letter in ascii_lowercase:
                result[letter] = result.get(letter, 0) + text.count(letter)

    result = list(zip(result.keys(), result.values()))
    result.sort(key=operator.itemgetter(1))

    return result[-5::]


# print(wordcount('wcfile.txt'))
# print(count_word())

# print(files_size())
print(letter_frequency())