#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29: sum_numbers"""


def sum_numbers(numbers):
    """Takes a string containing space-separated words.
    Output is an integer, the sum of those words that can
    be turned into integers.
    """
    return sum(int(x) for x in numbers.split() if x.isdigit())


def vowels():
    """
    Show the lines of a text file that contain at least one vowel and contain more
    than 20 characters
    """
    with open('shoe-data.txt') as file:
        result = [line for line in file if len(line) > 20 and ('a' in line
                                                               or 'e' in line
                                                               or 'u' in line
                                                               or 'i' in line
                                                               or 'o' in line)]

    return result


def phone_conversion(_list):
    """
    In the United States, phone numbers have 10 digits—a three-digit area code,
    followed by a seven-digit number. Several times during my childhood, area
    codes would run out of phone numbers, forcing half of the population to get a
    new area code. After such a split, XXX-YYY-ZZZZ might remain XXX-YYY-ZZZZ,
    or it might become NNN-YYY-ZZZZ, with NNN being the new area code. The
    decision regarding which numbers remained and which changed was often
    made based on the phone numbers’ final seven digits. Use a list comprehension
    to return a new list of strings, in which any phone number whose YYY begins
    with the digits 0–5 will have its area code changed to XXX+1. For example,
    given the list of strings ['123-456-7890', '123-333-4444', '123-777-8888'],
    we want to convert them to ['124-456-7890', '124-333-4444', '124-777-
    8888'].
    """
    _list = [y for number in _list for y in number]

    print(_list)


def dicts_manipulation():
    """
    Define a list of five dicts. Each dict will have two key-value pairs, name and age,
    containing a person’s name and age (in years). Use a list comprehension to
    produce a list of dicts in which each dict contains three key-value pairs:
    the original name, the original age, and a third age_in_months key,
    containing the person’s age in months. However, the output should exclude any of the input dicts
    representing people over 20 years of age.
    """
    _dict = [{'name': "Bill", 'age': 15},
             {'name': "Andrew", 'age': 40},
             {'name': "Alex", 'age': 50},
             {'name': "Max", 'age': 18},
             {'name': "Mike", 'age': 35}]

    return [{'name': person['name'], 'age': person['age'], 'age_months': person['age'] * 12}
            for person in _dict if person['age'] > 20]

# print(sum_numbers('10 abc 20 de44 30 55fg 40'))
# print(vowels())
# print(phone_conversion(['123-456-7890', '123-333-4444', '123-777-8888']))
print(dicts_manipulation())
