#!/usr/bin/env python3

"""Solution to chapter 10, exercise 48: all_lines"""


from pathlib import Path


def all_lines(path):
    """An iterator that returns, one at a time, each line
    from each file in a named directory.
    Any file that cannot be opened, for whatever reason, is ignored.
    """
    pth = Path(path)

    files = (file for file in pth.iterdir() if file.is_file())

    for file in files:
        for line in open(file, encoding='utf-8'):
            yield line


def all_lines_tuple(path):
    """
    Modify all_lines such that it doesn’t return a string with each iteration, but
    rather a tuple. The tuple should contain four elements: the name of the file,
    the current number of the file (from all those returned by os.listdir), the
    line number within the current file,
    """
    pth = Path(path)

    files = (file for file in pth.iterdir() if file.is_file())

    for index, file in enumerate(files):
        for line_num, line in enumerate(open(file, encoding='utf-8')):
            yield file.name, index + 1, line_num + 1, line


def all_lines_diff_order(path):
    """
    The current version of all_lines returns all of the lines from the first file, then
    all of the lines from the second file, and so forth. Modify the function such that it
    returns the first line from each file, and then the second line from each file, until
    all lines from all files are returned. When you finish printing lines from shorter
    files, ignore those files while continuing to display lines from the longer files
    """
    pth = Path(path)

    files = [file for file in pth.iterdir() if file.is_file()]
    res = [[] for _ in files]
    for file_index, file in enumerate(files):
        for line in open(file):
            res[file_index].append(line)

    max_len = max(len(arr) for arr in res)

    for line in range(0, max_len):
        for arr in res:
            try:
                yield arr[line].strip()
            except IndexError:
                pass


def all_lines_with_filter(path, string):
    """Modify all_lines such that it takes two arguments—a directory name, and a
    string. Only those lines containing the string (i.e., for which you can say s in
    line) should be returned. If you know how to work with regular expressions
    and Python’s re module, then you could even make the match conditional on a
    regular expression."""

    pth = Path(path)

    files = (file for file in pth.iterdir() if file.is_file())

    for file in files:
        for line in open(file, encoding='utf-8'):
            if string in line:
                yield line.strip()


for one in all_lines_with_filter('../ch08-modules', 'return'):
    print(one)
