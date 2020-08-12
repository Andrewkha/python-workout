#!/usr/bin/env python3
"""Solution to chapter 2, exercise 8: strsort"""


def strsort(a_string):
    """Takes a string as input,
returns a string with its characters sorted.
"""
    return ''.join(sorted(a_string))


def words(_string: str) -> str:
    """
    Given the string “Tom Dick Harry,” break it into individual words, and then sort
    those words alphabetically. Once they’re sorted, print them with commas (,)
    between the names
    """
    words_list = _string.split()
    words_list.sort()
    return ','.join(words_list)


def last_word_text():
    """
    Which is the last word, alphabetically, in a text file?
    """
    with open('../files/61105-0.txt', encoding='utf-8') as file:
        text = file.read()
    text_words = text.split()

    return max(text_words)


def longest_word():
    """
    Which is the longest word in a text file?
    """
    with open('../files/61105-0.txt', encoding='utf-8') as file:
        text = file.read()
    text_words = text.split()
    text_words.sort(key=lambda x: len(x))

    return text_words[-1]


print(strsort('azsxdcfvgbghew'))
print(words('Tom Dick Harry'))
print(last_word_text())
print(longest_word())