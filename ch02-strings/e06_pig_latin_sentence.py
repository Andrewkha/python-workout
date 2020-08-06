#!/usr/bin/env python3
"""Solution to chapter 2, exercise 6: pl_sentence"""

from e05_pig_latin import pig_latin


def pl_sentence(sentence: str):
    """Get a sentence from the user, containing
lowercase, unpuncutated words. Return the
sentence, translated into Pig Latin.
"""
    result = []
    for one in sentence.split():
        result.append(pig_latin(one))

    return ' '.join(result)


def sentence_from_text(n):
    """Take a text file, creating (and printing) a nonsensical sentence from the nth
    word on each of the first 10 lines, where n is the line number."""
    with open('../files/61105-0.txt', encoding='utf-8') as file:
        text = file.readlines()

    sentence = []
    if text:
        for index, line in enumerate(text):
            words = line.split()
            if len(words) >= n:
                sentence.append(words[n - 1])
            if index == 10:
                break

    return ' '.join(sentence)


def transpose(lst: list):
    """Write a function that transposes a list of strings, in which each string contains
    multiple words separated by whitespace. Specifically, it should perform in such a
    way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']."""

    result = [[] for _ in lst]

    for item in lst:
        for index, word in enumerate(item.split()):
            result[index].append(word)

    for index, item in enumerate(result):
        result[index] = ' '.join(item)

    return result


print(pl_sentence("this is a test translation"))
print(sentence_from_text(1))
print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
