#!/usr/bin/env python3

"""Solution to chapter 7, exercise 34: get_sv"""


def get_sv(filename):
    """Given a filename (string) as input,
    this function returns a set of all words
    in which all five vowels can be found.
    """
    vowels = {'a', 'e', 'u', 'i', 'o'}
    with open(filename) as file:
        return {word.strip() for word in file if vowels < set(word)}


def lnx_shells():
    """
    In the /etc/passwd file you used earlier, what different shells (i.e., command
    interpreters, named in the final field on each line) are assigned to users? Use a
    set comprehension to gather them
    """
    with open('passwords.txt') as file:
        return {line.split(':')[-1].strip() for line in file if len(line.split(':')) > 1}


def words_length():
    """
    Given a text file, what are the lengths of the different words?
     Return a set of different word lengths in the file
    """

    with open('words.txt') as file:
        return {len(word) for word in file.read().split()}


def letters_in_names():
    """
    Create a list whose elements are strings—the names of people in your family.
    Now use a set comprehension (and, better yet, a nested set comprehension) to
    find which letters are used in your family members’ names.
    """
    names = ['Andrey', "Alena", 'Dima']

    return {letter for name in names for letter in name}


# print(get_sv('words.txt'))
# print(lnx_shells())
# print(words_length())
print(letters_in_names())
