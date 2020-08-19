#!/usr/bin/env python3
"""Solution to chapter 5, exercise 22: passwd_to_csv"""


import csv


def passwd_to_csv(passwd_filename, csv_filename):
    """Function that takes the filename of a
Unix-style passwd file to be read from, and the
name of a file that will be created and written to.
The username and user ID from the passwd file will
be written to the second file in CSV format, with
a tab separator.
"""
