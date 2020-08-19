#!/usr/bin/env python3
"""Solution to chapter 4, exercise 17: different_numbers"""

import re
from pathlib import Path

def how_many_different_numbers(numbers):
    """Takes a list of numbers as input.
    Returns the number of different numbers in that list.
    """
    return len(set(numbers))


def apache_ip():
    """Read through a server (e.g., Apache or nginx) log file. What were the different
    IP addresses that tried to access your server?"""
    pattern_ip = re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
    ips = set()
    with open('C:\\xampp\\apache\\logs\\access.log') as file:
        for line in file.readlines():
            m = pattern_ip.match(line)
            if m:
                ips.add(m.group())

    return ips


def apache_response():
    """
    Reading from that same server log, what response codes were returned to
    users? The 200 code represents “OK,” but there are also 403, 404, and 500
    errors. (Regular expressions aren’t required here but will probably help.)
    """
    codes = set()
    with open('C:\\xampp\\apache\\logs\\access.log') as file:
        for line in file.readlines():
            codes.add(line.split()[8])
    return codes


def filenames():
    """
    Use os.listdir (http://mng.bz/YreB) to get the names of files in the current
    directory. What file extensions (i.e., suffixes following the final . character)
    appear in that directory? It’ll probably be helpful to use os.path.splitext
    (http://mng.bz/GV4v).
    """
    for one in Path.cwd().iterdir():
        print(one.name)
        print(one.suffix)


# print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))
# print(apache_ip())
# print(apache_response())
filenames()
