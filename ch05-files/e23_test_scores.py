#!/usr/bin/env python3
"""Solution to chapter 5, exercise 23: test_scores"""

import json
import csv
from pathlib import Path
import operator


def print_scores(dirname):
    """Takes the name of a directory containing
    one or more JSON files with a ".json" suffix.
    The files contain test scores in a variety of
    subjects.

    For each class, the function prints the min,
    max, and average score for each subject.
    """
    for file in Path(dirname).glob('*.json'):
        with open(file) as f:
            scores = {}
            for one in json.load(f):
                for subj, score in one.items():
                    scores[subj] = scores.get(subj, []) + [score]

        print(Path(dirname) / file.name)
        for subj, score in scores.items():
            print(f"{subj}: min {min(score)}, max {max(score)}, average {sum(score) / len(score)}")


def from_csv_to_json():
    """Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
    JSON file will contain the equivalent of a list of Python tuples, with each tuple
    representing one line from the file"""

    with open('linux-etc-passwd.txt') as file, open('linux-etc-passwd.json', 'w') as file1:
        in_file = [x for x in list(csv.reader(file, delimiter=':')) if len(x) > 1]
        json.dump(in_file, file1)


def from_csv_to_dict_json():
    """
    For a slightly different challenge, turn each line in the file into a Python dict.
    This will require identifying each field with a unique column or key name. If
    you’re not sure what each field in /etc/passwd does, you can give it an arbitrary name.
    """
    output = []
    fields = ['name', 'id1', 'id2', 'id3', 'alias', 'home_path', 'shell']
    with open('linux-etc-passwd.txt') as file, open('linux-etc-passwd-dict.json', 'w') as file1:
        in_file = csv.reader(file, delimiter=':')
        for line in in_file:
            if len(line) > 1:
                output.append({value: line[pos] for pos, value in enumerate(fields)})

        json.dump(output, file1)


def file_info_to_json(directory):
    """
    Ask the user for the name of a directory. Iterate through each file in that directory (ignoring subdirectories),
    getting (via os.stat) the size of the file and when it was last modified. Create a JSON-formatted file on disk
    listing each filename, size, and modification timestamp. Then read the file back in, and identify which
    files were modified most and least recently, and which files are largest
    and smallest, in that directory.
    """
    data = []

    for file in Path(directory).iterdir():
        if file.is_file():
            data.append({'name': file.name,
                         'size': file.stat().st_size,
                         'last_changed': file.stat().st_ctime})

    with open(Path(directory) / 'file_info.json', 'w+') as file:
        json.dump(data, file)
        file.seek(0)
        new_data = json.load(file)

    last_modified = max(new_data, key=operator.itemgetter('last_changed'))
    least_modified = min(new_data, key=operator.itemgetter('last_changed'))
    largest_file = max(new_data, key=operator.itemgetter('size'))
    print(last_modified)
    print(least_modified)
    print(largest_file)


file_info_to_json('.')
