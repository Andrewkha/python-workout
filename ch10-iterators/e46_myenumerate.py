#!/usr/bin/env python3

"""Solution to chapter 10, exercise 46: myenumerate"""


class MyEnumerate:
    """Simple replacement for enumerate"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = (self.index, self.data[self.index])
        except IndexError:
            raise StopIteration

        self.index += 1
        return value


for one in MyEnumerate('asdf'):
    print(one)


"""
Rewrite MyEnumerate such that it uses a helper class (MyEnumerateIterator), as
described in the “Discussion” section. In the end, MyEnumerate will have the
__iter__ method that returns a new instance of MyEnumerateIterator, and the
helper class will implement __next__. It should work the same way, but will also
produce results if we iterate over it twice in a row."""

class MyEnumerate2:
    """Simple replacement for enumerate"""

    def __init__(self, data, index=0):
        self.data = data
        self.index = index

    def __iter__(self):
        return MyEnumerateIterator(self.data, self.index)


class MyEnumerateIterator:

    def __init__(self, data, index):
        self.data = data
        self.start = self.index = index

    def __next__(self):
        try:
            value = (self.index, self.data[self.index - self.start])
        except IndexError:
            raise StopIteration

        self.index += 1
        return value


e = MyEnumerate2('abc')
print('** A **')
for index, one_item in e:
    print(f'{index}: {one_item}')

print('** B **')
for index, one_item in e:
    print(f'{index}: {one_item}')


def my_enumerate(data, start=0):
    """Redefine MyEnumerate as a generator function, rather than as a class."""
    index = start
    for item in data:
        yield index, item
        index += 1


for one in my_enumerate('asad', 5):
    print(one)
