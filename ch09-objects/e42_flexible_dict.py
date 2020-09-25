#!/usr/bin/env python3

"""Solution to chapter 9, exercise 42: flexible dict"""


class FlexibleDict(dict):
    """Dict that lets you use a string or int somewhat interchangeably."""

    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)


class StrictDict(dict):
    """
    With FlexibleDict, we allowed the user to use any key, but were then flexible
    with the retrieval. Implement StringKeyDict, which converts its keys into
    strings as part of the assignment. Thus, immediately after saying skd[1] = 10,
    you would be able to then say skd['1'] and get the value of 10 returned. This
    can come in handy if you’ll be reading keys from a file and won’t be able
    to distinguish between strings and integers
    """

    def __setitem__(self, key, value):
        try:
            key = str(key)
        except ValueError:
            pass

        dict.__setitem__(self, key, value)


class RecentDict(dict):
    """
    The RecentDict class works just like a dict, except that it contains a user defined
    number of key-value pairs, which are determined when the instance is
    created. In a RecentDict(5), only the five most recent key-value pairs are kept;
    if there are more than five pairs, then the oldest key is removed, along with its
    value. Note: your implementation could take into account the fact that modern
    dicts store their key-value pairs in chronological order.
    """

    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def __setitem__(self, key, value):
        if len(self) >= self.limit:
            for k, _ in self.items():
                first_key = k
                break
            dict.__delitem__(self, first_key)

        dict.__setitem__(self, key, value)


class FlatList(list):
    """
    The FlatList class inherits from list and overrides the append method. If
    append is passed an iterable, then it should add each element of the iterable
    separately. This means that fl.append([10, 20, 30]) would not add the list
    [10, 20, 30] to fl, but would rather add the individual integers 10, 20, and 30.
    You might want to use the built-in iter function (http://mng.bz/Qy2G) to
    determine whether the passed argument is indeed iterable.
    """

    def append(self, __object):
        try:
            for element in __object:
                super().append(element)
        except TypeError:
            super().append(__object)


if __name__ == '__main__':
    # d = FlexibleDict({'1': 1, 2: '2'})
    #
    # print(d[1])
    # print(d['1'])
    # print(d[2])
    # print(d['2'])
    #
    # s = StrictDict()
    #
    # s[1] = 2
    # s[(1, 2, 3)] = 3
    #
    # print(s)
    # recent_dict = RecentDict(2)
    # recent_dict[1] = 4
    # recent_dict[2] = 3
    # recent_dict[3] = 2
    # recent_dict[4] = 1
    #
    # print(recent_dict)
    flat = FlatList()
    flat.append(4)
    flat.append([1, 2, 3])
    flat.append((4, 5))
    flat.append('asd')

    print(flat)

