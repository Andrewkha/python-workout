#!/usr/bin/env python3
"""Solution to chapter 5, exercise 23: test_scores"""

import json
import glob


def print_scores(dirname):
    """Takes the name of a directory containing
one or more JSON files with a ".json" suffix.
The files contain test scores in a variety of
subjects.

For each class, the function prints the min,
max, and average score for each subject.
"""

