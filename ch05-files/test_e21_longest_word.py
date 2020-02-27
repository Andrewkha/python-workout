from e21_longest_word import find_longest_word, find_all_longest_words
import pytest
from io import StringIO


@pytest.fixture
def empty_file(tmp_path):
    f = tmp_path / 'emptyfile.txt'
    f.write_text('')
    return f


@pytest.fixture
def small_file(tmp_path):
    f = tmp_path / 'smallfile.txt'
    f.write_text('''This is the first line
and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f


@pytest.fixture
def big_file(tmp_path):
    f = tmp_path / 'bigfile.txt'
    f.write_text('''This is the first line of a big file

and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f
