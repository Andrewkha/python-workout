#!/usr/bin/env python3
"""Solution to chapter 2, exercise 5: pig_latin"""


def pig_latin(word):
    """Translates a word into Pig Latin.
The "word" parameter is assumed to be an
English word, returned as a string"""
    if word[0] in 'aeuio':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'


def capitalized_pig_latin(word: str):
    return pig_latin(word).capitalize() if word[0].isupper() and word[1:].islower() else pig_latin(word)


import string

def punctuation_pig_latin(word):

    if word[-1] in string.punctuation:
        subword = word[0:-1]
        return pig_latin(subword) + word[-1]
    else:
        return pig_latin(word)


def alternative(word):
    """Consider an alternative version of Pig Latin—We don’t check to see if the first letter
is a vowel, but, rather, we check to see if the word contains two different vowels.
If it does, we don’t move the first letter to the end. Because the word “wine”
contains two different vowels (“i” and “e”), we’ll add “way” to the end of it, giving us “wineway.” By contrast, the word “wind” contains only one vowel, so we
would move the first letter to the end and add “ay,” rendering it “indway.” How
would you check for two different vowels in the word? (Hint: sets can come in
handy here.)"""
    vowels = []
    for char in word:
        if char in 'aeuio':
            vowels.append(char)
    if len(set(vowels)) == 2:
        return word + 'way'
    else:
        return pig_latin(word)


print(pig_latin('eat'))
print(capitalized_pig_latin('Computer'))
print(capitalized_pig_latin('computer'))
print(punctuation_pig_latin('computer.'))
print(alternative('wine'))
print(alternative('wind'))
