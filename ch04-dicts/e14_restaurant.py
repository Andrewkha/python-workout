#!/usr/bin/env python3
"""Solution to chapter 4, exercise 14: restaurant"""

import getpass
from datetime import date

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}
USERS = {'mary': 'mary_pass', 'john': 'john_pass', 'donald': 'donald_pass'}


def restaurant():
    """Ask the user to enter their dining preferences, one by one, based
on the global "MENU" dict.

- If the user enters an empty string, stop asking and print the total bill.
- If the user enters something on the menu (i.e., a key in "MENU"), then
  print the price and the total.
- If the user enters something not on the menu, then tell them the item isn't
  available.
"""
    total = 0

    while True:
        order = input('Your order? :').strip()
        if not order:
            break
        if order in MENU:
            price = MENU.get(order)
            total += price
            print(f"{order} costs {price}, total {total}")
        else:
            print(f"We do not have {order}")

    print(f"Your total is {total}")


def login():
    """
    Create a dict in which the keys are usernames and the values are passwords,
    both represented as strings. Create a tiny login system, in which the user must
    enter a username and password. If there is a match, then indicate that the user
    has successfully logged in. If not, then refuse them entry. (Note: This is a nice
    little exercise, but please never store unencrypted passwords. It’s a major security risk.)
    """
    name = input('Provide your name: ')
    passwd = input('Provide you pass: ')

    if USERS.get(name) == passwd:
        print("welcome")
    else:
        print('fuckoff')


def login_better():
    """
    Create a dict in which the keys are usernames and the values are passwords,
    both represented as strings. Create a tiny login system, in which the user must
    enter a username and password. If there is a match, then indicate that the user
    has successfully logged in. If not, then refuse them entry. (Note: This is a nice
    little exercise, but please never store unencrypted passwords. It’s a major security risk.)
    using asterisk for password
    """
    name = input('Provide your name: ')
    passwd = getpass.getpass(prompt="Please enter password: ")

    if USERS.get(name) == passwd:
        print("welcome")
    else:
        print('fuckoff')


def days_live():
    """
    Define a dict whose keys are names of people in your family, and whose values
    are their birth dates, as represented by Python date objects (http://mng.bz/
    jggr). Ask the user to enter the name of someone in your family, and have the
    program calculate how many days old that person is
    """
    birth_dates = {
        'Andrey': date(1981, 9, 9),
        'Alena': date(1981, 10, 15),
        'Dima': date(2015, 10, 6),
    }

    name = input("Please enter a name: ")
    birth_date = birth_dates.get(name)

    if birth_date:
        diff = date.today() - birth_date
        print(diff.days)
    else:
        print("No such person")


# restaurant()
# login()
# login_better()
days_live()
