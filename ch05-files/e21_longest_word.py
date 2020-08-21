#!/usr/bin/env python3
"""Solution to chapter 5, exercise 21: longest_word"""

from pathlib import Path
from hashlib import md5
import arrow


def find_longest_word(filename):
    """Given a filename, return the longest word in the file."""
    with open(filename, encoding='utf-8') as file:
        words = file.read().split()

    return max(words, key=len)


def find_all_longest_words(dirname):
    """Given a directory name, return a dict in which the keys
are filenames in the directory and the values are
    the strings -- the longest word in each file."""
    files = Path(dirname).iterdir()
    result = {file.name: find_longest_word(file) for file in files}

    return result


def get_hashes(dirname):
    """
    Use the hashlib module in the Python standard library, and the md5 function
    within it, to calculate the MD5 hash for the contents of every file in a user
    specified directory. Then print all of the filenames and their MD5 hashes.
    """
    result = {}
    for file in Path(dirname).iterdir():
        with open(file, encoding='utf-8') as _file:
            text = _file.read()
            result[file.name] = md5(text.encode('utf-8'))

    return result


def dir_change_date(dirname):
    """
    Ask the user for a directory name. Show all of the files in the directory, as well
    as how long ago the directory was modified
    """
    changed = arrow.get(Path(dirname).stat().st_ctime).format('YYYY-MM-DD HH:mm')
    print(changed)
    for file in Path(dirname).iterdir():
        print(file.name)


def http_log_parse():
    """
    Open an HTTP server’s log file. (If you lack one, then you can read one from
    me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
    response codes—202, 304, and so on
    """
    result = {}
    with open('mini-access-log.txt') as file:
        text = file.readlines()

    for line in text:
        status_code = line.split()[8]
        result[status_code] = result.get(status_code, 0) + 1

    return result


# print(find_all_longest_words("../files"))
# print(get_hashes("../files"))
dir_change_date('../files')
print(http_log_parse())