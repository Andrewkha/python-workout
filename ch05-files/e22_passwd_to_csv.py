#!/usr/bin/env python3
"""Solution to chapter 5, exercise 22: passwd_to_csv"""


import csv
import random


def passwd_to_csv(passwd_filename, csv_filename):
    """Function that takes the filename of a
    Unix-style passwd file to be read from, and the
    name of a file that will be created and written to.
    The username and user ID from the passwd file will
    be written to the second file in CSV format, with
    a tab separator.
    """
    result = []
    with open(passwd_filename) as file:
        passwd_lines = file.readlines()

    for line in passwd_lines:
        if line.strip() and not line.startswith("#"):
            user, passwd = line.split(":")[0], line.split(":")[2]
            result.append((user, passwd))

    with open(csv_filename, 'w', newline='') as file:
        output = csv.writer(file, delimiter='\t')
        output.writerows(result)


def passwd_to_csv_alternative(passwd_filename, csv_filename):
    """Function that takes the filename of a
    Unix-style passwd file to be read from, and the
    name of a file that will be created and written to.
    The username and user ID from the passwd file will
    be written to the second file in CSV format, with
    a tab separator.
    """
    with open(passwd_filename) as passwd, open(csv_filename, 'w', newline='') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


def passwd_to_csv_custom(passwd_filename, csv_filename):
    """
    Extend this exercise by asking the user to enter a space-separated list of integers,
    indicating which fields should be written to the output CSV file. Also ask
    the user which character should be used as a delimiter in the output file. Then
    read from /etc/passwd, writing the user’s chosen fields, separated by the user’s
    chosen delimiter.
    """
    fields = input('Please provide fields numbers to use: ')
    separator = input('Please provide a separation character: ')
    fields = list(map(int, fields.split()))
    with open(passwd_filename) as passwd, open(csv_filename, 'w', newline='') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=separator)
        for record in infile:
            if len(record) > 1:
                outfile.writerow(record[x] for x in fields)


def dict_to_csv():
    """
    Write a function that writes a dict to a CSV file. Each line in the CSV file should
    contain three fields: (1) the key, which we’ll assume to be a string, (2) the value,
    and (3) the type of the value (e.g., str or int).
    """
    _dict = {'sandwich': 10, 'tea': 7, 'salad': 9, 'swewe': 'sdsdr', 'wew': 12, 'dsaer': 'wered'}
    with open('dict_to_csv.csv', 'w', newline='') as file:
        outfile = csv.writer(file)
        for key, value in _dict.items():
            outfile.writerow((key, value, type(value)))


def random_to_csv():
    """
    Create a CSV file, in which each line contains 10 random integers between 10
    and 100. Now read the file back, and print the sum and mean of the numbers
    on each line.
    """

    with open('randints.csv', 'w', newline='') as file:
        out = csv.writer(file)
        for _ in range(10):
            out.writerow([random.randint(10, 100) for x in range(10)])

    with open('randints.csv') as file:
        _in = csv.reader(file)
        for line in _in:
            ints = [int(x) for x in line]
            print(sum(ints), sum(ints) / len(ints))


# passwd_to_csv('linux-etc-passwd.txt', 'pass.csv')
# passwd_to_csv_custom('linux-etc-passwd.txt', 'pass.csv')
# passwd_to_csv_alternative('linux-etc-passwd.txt', 'pass.csv')
# dict_to_csv()
random_to_csv()
