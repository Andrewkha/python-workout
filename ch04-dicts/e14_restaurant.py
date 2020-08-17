#!/usr/bin/env python3
"""Solution to chapter 4, exercise 14: restaurant"""


MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def restaurant():
    """Ask the user to enter their dining preferences, one by one, based
on the global "MENU" dict.

- If the user enters an empty string, stop asking and print the total bill.
- If the user enters something on the menu (i.e., a key in "MENU"), then
  print the price and the total.
- If the user enters something not on the menu, then tell them the item isn't
  available.
"""


