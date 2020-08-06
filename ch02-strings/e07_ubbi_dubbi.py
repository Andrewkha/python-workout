#!/usr/bin/env python3
"""Solution to chapter 2, exercise 7: ubbi_dubbi"""


def ubbi_dubbi(word):
    """Ask the user to enter a word,
and return the word's translation into Ubbi Dubbi.
"""
    vowels = 'aeuio'
    result = []

    for char in word:
        to_add = f"ub{char}" if char in vowels else char
        result.append(to_add)

    return ''.join(result)


def ubbi_dubbi_capitalize(word: str):
    """
    Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn’t), then the Ubbi Dubbi translation should be
    similarly capitalized
    """

    capital = True if word[0].isupper() and word[1:].islower() else False

    ubbi_word = ubbi_dubbi(word.lower())
    ubbi_word = ubbi_word.capitalize() if capital else ubbi_word

    return ubbi_word


def url_encode(line: str):
    """
    URL-encode characters—In URLs, we often replace special and nonprintable
    characters with a % followed by the character’s ASCII value in hexadecimal. For
    example, if a URL is to include a space character (ASCII 32, aka 0x20), we
    replace it with %20. Given a string, URL-encode any character that isn’t a letter
    or number. For the purposes of this exercise, we’ll assume that all characters
    are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It
    might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng.bz/nPxg) functions
    """

    from string import ascii_letters
    numbers = '0123456789'

    result = []

    for char in line:
        if char in ascii_letters or char in numbers:
            result.append(char)
        else:
            result.append(f"%{hex(ord(char))}%")

    return ''.join(result)

print(ubbi_dubbi('octopus'))
print(ubbi_dubbi('elephant'))
print(ubbi_dubbi_capitalize('elephant'))
print(ubbi_dubbi_capitalize('Elephant'))
print(url_encode("asa ds dsd"))
