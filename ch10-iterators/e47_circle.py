#!/usr/bin/env python3

"""Solution to chapter 10, exercise 47: circle"""


class CircleIterator:
    """Iterator for Circle."""

    def __init__(self, data, max_times):
        self.max_times = max_times
        self.data = data * (max_times // len(data) + 1)
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration

        value = self.data[self.index]
        self.index += 1

        return value


class Circle:
    """Class that produces an iterator, which repeatedly cycles
    through the elements of an iterator until returning max_times
    items. """

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)

# c = Circle('asdsdsd', 45)
# print(list(c))


class Circle2(CircleIterator):
    """Rather than write a helper, you could also define iteration capabilities in a class
    and then inherit from it. Reimplement Circle as a class that inherits from
    CircleIterator, which implements __init__ and __next__. Of course, the
    parent class will have to know what to return in each iteration;
    add a new attribute in Circle, self.returns, a list of attribute names that should be returned."""

    def __iter__(self):
        return self

# c = Circle2('asds', 3)
# print(list(c))


def circle_generator(data, max):
    data = data * (max // len(data) + 1)
    for index, item in enumerate(data):
        if index < max:
            yield item


# print(list(circle_generator('sadfg', 7)))


class MyRange:
    """Implement a MyRange class that returns an iterator that works the same as
    range, at least in for loops. (Modern range objects have a host of other capabilities,
    such as being subscriptable. Don’t worry about that.) The class, like range,
    should take one, two, or three integer arguments"""

    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start + self.count * self.step < self.end:
            current_step = self.count
            self.count += 1
            return self.start + current_step * self.step

        raise StopIteration


print(list(MyRange(2, 10, 4)))
