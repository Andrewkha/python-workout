#!/usr/bin/env python3

import operator

"""Solution to chapter 7, exercise 29: flatten"""


def flatten(mylist):
    """Expects to get a nested list (a list of lists)
    as input. Returns a flattened list, containing the
    elements of mylist in order, as output.
    """
    return [y for x in mylist for y in x]


def flatten_odd_ints(mylist):
    """
    Write a version of the flatten function mentioned earlier called flatten_odd
    _ints. It’ll do the same thing as flatten, but the output will only contain odd
    integers. Inputs that are neither odd nor integers should be excluded. Inputs
    containing strings that could be converted to integers should be converted;
    other strings should be excluded.
    """

    return [int(y) for x in mylist for y in x if str(y).isdigit() and int(y) % 2 == 0]


def children_grandchildren():
    """
    Define a dict that represents the children and grandchildren in a family. (See
    figure 7.1 for a graphic representation.) Each key will be a child’s name, and
    each value will be a list of strings representing their children (i.e., the family’s
    grandchildren). Thus the dict {'A':['B', 'C', 'D'], 'E':['F', 'G']} means
    Iterates through each element of mylist  Iterates through each
    element of one_sublistEXERCISE 31 ■ Pig Latin translation of a file 129
    that A and E are siblings; A’s children are B, C, and D; and E’s children are F and
    G. Use a list comprehension to create a list of the grandchildren’s names
    """
    kids = {"Andrey": ['Ilya', "Dima"], 'Miha': ['Vanya', 'Petya', 'Kolya'], 'Olga': ['Kira']}

    return [grand_kid for kid, grand_kids in kids.items() for grand_kid in grand_kids]


def children_grandchildren_extended():
    """
    Redo this exercise, but replace each grandchild’s name (currently a string) with
    a dict. Each dict will contain two name-value pairs, name and age. Produce a list
    of the grandchildren’s names, sorted by age, from eldest to youngest
    """
    kids = {"Andrey": [{'name': 'Ilya', 'age': 6},
                       {'name': "Dima", 'age': 4}],
            'Miha': [{'name': 'Vanya', 'age': 10},
                     {'name': 'Petya', 'age': 3},
                     {'name': 'Kolya', 'age': 1}],
            'Olga': [{'name': 'Kira', 'age': 5}]}

    kids = [grand_kid for kid, grand_kids in kids.items() for grand_kid in grand_kids]
    kids = sorted(kids, key=operator.itemgetter('age'))
    return [x['name'] for x in kids]


print(flatten([[1, 2, 3, 4, 5], [5, 2, 4, 6, 2], [3, 5, 3, 1, 3]]))
print(flatten_odd_ints([[1, '2', 'sdsds', 4, 5], ['5ddd', 2, 4, '6', 2], [3, 5, 3, 1, 3]]))
print(children_grandchildren())
print(children_grandchildren_extended())

