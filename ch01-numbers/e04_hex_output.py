#!/usr/bin/env python3
"""Solution to chapter 1, exercise 4: hex_output"""
"""Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth, until the entire name is written on the final line."""


def name_triangle(name):
    output = ''
    for char in name:
        output += char
        print(output)


name_triangle('Andrewkha')