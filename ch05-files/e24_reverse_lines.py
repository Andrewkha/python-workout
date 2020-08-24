#!/usr/bin/env python3
"""Solution to chapter 5, exercise 24: reverse_lines"""

import csv


def reverse_lines(infilename, outfilename):
    """Takes two filenames as arguments. The
    first is for reading, and the second is for writing.
    The contents of the first file are written to
    the second, but in reverse order.
    """
    with open(infilename) as file_in:
        text_lines = file_in.readlines()

    text_lines = [x[::-1].strip() for x in text_lines]

    with open(outfilename, 'w') as file_out:
        file_out.write('\n'.join(text_lines))


def encrypt_file():
    """
    “Encrypt” a text file by turning all of its characters into their numeric equivalents
    (with the built-in ord function) and writing that file to disk. Now “decrypt”
    the file (using the built-in chr function), turning the numbers back into their
    original characters
    """
    with open('wcfile.txt') as read_file, open('wcfile_enc.txt', 'w') as to_file:
        for character in read_file.read():
            to_file.write(str(ord(character)) + ' ')

    with open('wcfile_enc.txt') as read_file, open('wcfile_dec.txt', 'w') as to_file:
        for char in read_file.read().split():
            to_file.write(str(chr(int(char))))


def split_file_in_two(file):
    """
    Given an existing text file, create two new text files. The new files will each contain the
    same number of lines as the input file. In one output file, you’ll write
    all of the vowels (a, e, i, o, and u) from the input file. In the other, you’ll write
    all of the consonants. (You can ignore punctuation and whitespace.)
    """
    vowels = 'aeiou\n'
    consonants = 'qwrtypsdfghjklzxcvbnm\n'
    out_vowels = []
    out_consonants = []

    with open(file) as input_file, \
            open('vowels.txt', 'w') as vowels_file, \
            open('consonants.txt', 'w') as consonants_file:
        text = input_file.read()
        for character in text:
            if character in vowels:
                out_vowels.append(character)
            if character in consonants:
                out_consonants.append(character)

        vowels_file.write("".join(out_vowels))
        consonants_file.write("".join(out_consonants))


def shells_to_file():
    """
    The final field in /etc/passwd is the shell, the Unix command interpreter that’s
    invoked when a user logs in. Create a file, containing one line per shell, in
    which the shell’s name is written, followed by all of the usernames that use the
    shell; for example
    """
    results = {}
    with open('linux-etc-passwd.txt') as input_file, open('linux-shells-users.txt', 'w') as out_file:
        text = csv.reader(input_file, delimiter=':')
        for line in text:
            if len(line) > 1:
                results[line[-1]] = results.get(line[-1], []) + [line[0]]

        for shell, users in results.items():
            out_file.write(f"{shell}: {','.join(users)}\n")


# reverse_lines('output.txt', 'input.txt')
split_file_in_two('mini-access-log.txt')
print(shells_to_file.__code__.co_varnames)
