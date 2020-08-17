#!/usr/bin/env python3
"""Solution to chapter 3, exercise 13: tuple_records"""


import operator
from collections import namedtuple

person = namedtuple('person', 'first_name, last_name, distance')

PEOPLE = [('Voladimir', 'Putin', 3.626),
          ('Vlodimir', 'Putin', 3.626),
          ('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

PEOPLE2 = [person('Voladimir', 'Putin', 3.626),
           person('Vlodimir', 'Putin', 3.626),
           person('Donald', 'Trump', 7.85),
           person('Vladimir', 'Putin', 3.626),
           person('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples: list):
    """This function expects to get a list
    of tuples, each representing a person.

    Each tuple contains three elements -- first
    name, last name, and distance to travel.

    (The first two are strings, and the third is
    a float.)  We return a list of strings,
    sorted by last name and then first name.
    """

    for one in sorted(list_of_tuples, key=operator.itemgetter(1, 0)):
        print(f"{one[1]:10} {one[0]:10} {one[2]:5.2f}")


def format_sort_records_named_tuples(list_of_tuples: list):
    """This function expects to get a list
    of tuples, each representing a person.

    Each tuple contains three elements -- first
    name, last name, and distance to travel.

    (The first two are strings, and the third is
    a float.)  We return a list of strings,
    sorted by last name and then first name.
    """

    for one in sorted(list_of_tuples, key=operator.attrgetter('last_name', 'first_name')):
        print(f"{one.last_name:10} {one.first_name:10} {one.distance:5.2f}")


movie = namedtuple('movie', 'name, length, director')
MOVIES = [movie('kokoo', 120, 'Pupkin'),
          movie('kokoo', 130, 'Pupkin130'),
          movie('kokoo', 100, 'Pupkin100'),
          movie('hello world', 85, 'Pushlin'),
          movie('new killer', 77, 'Lermontov'),
          movie('happy NY', 210, 'Ryazanov'),
          movie('lalala', 120, 'Popkin'),
          movie('zuzuzuz', 120, 'Pzpkin'),
          ]

print(operator.itemgetter(MOVIES[0], (1, 2)))


def sort_movies(films):
    """
    Define a list of tuples, in which each tuple contains the name, length (in minutes), and director of the
    movies nominated for best picture Oscar awards last
    year. Ask the user whether they want to sort the list by title, length, or director’s
    name, and then present the list sorted by the user’s choice of axis.
    """

    sort_order = ''
    while sort_order not in ('name', 'length', 'director'):
        sort_order = input('Please provide the criteria to sort (name, length, director): ')

    return sorted(films, key=operator.attrgetter(sort_order))


def sort_movies_multiple(films):
    """
    Extend this exercise by allowing the user to sort by two or three of these fields,
    not just one of them. The user can specify the fields by entering them separated
    by commas; you can use str.split to turn them into a list
    """

    options = ('name', 'length', 'director')

    sort_order = ''

    while not sort_order:
        sort_order = input('Please provide the criteria to sort (name, length, director): ')

    selected_options = [x for x in sort_order.split(',') if x in options]

    return sorted(films, key=operator.attrgetter(*selected_options)) if selected_options else films


format_sort_records(PEOPLE)
format_sort_records_named_tuples(PEOPLE2)
# print(sort_movies(MOVIES))
print(sort_movies_multiple(MOVIES))
