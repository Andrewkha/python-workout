#!/usr/bin/env python3
"""Solution to chapter 3, exercise 10: mysum"""


def mysum(*items):
    """Sum the passed arguments, which should be of the same type.
    The arguments should handle the + operator.
    If passed no arguments, then return an empty tuple.
    """
    if not items:
        return tuple()
    summ = items[0]
    for element in items[1:]:
        summ += element

    return summ


def my_sum_bigger_than(threshold, *args):
    """
    Write a function, mysum_bigger_than, that works the same as mysum, except that
    it takes a first argument that precedes *args. That argument indicates the
    threshold for including an argument in the sum. Thus, calling mysum_bigger
    _than(10, 5, 20, 30, 6) would return 50—because 5 and 6 aren’t greater than
    10. This function should similarly work with any type and assumes that all of the
    arguments are of the same type. Note that > and < work on many different types
    in Python, not just on numbers; with strings, lists, and tuples, it refers to their
    sort order
    """
    if not args:
        return tuple()

    args = [x for x in args if x > threshold]
    summ = args[0]
    for element in args[1:]:
        summ += element

    return summ


def sum_numeric(*args):
    """
    Write a function, sum_numeric, that takes any number of arguments. If the
    argument is or can be turned into an integer, then it should be added to the
    total. Arguments that can’t be handled as integers should be ignored. The
    result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30',
    'bcd') would return 60. Notice that even if the string 30 is an element in the
    list, it’s converted into an integer and added to the total.
    """
    summ = 0
    for one in args:
        try:
            digit = int(one)
            summ += digit
        except:
            continue
    return summ


def join_dicts(list_of_dicts):
    """
    Write a function that takes a list of dicts and returns a single dict that combines
    all of the keys and values. If a key appears in more than one argument, the
    value should be a list containing all of the values from the arguments
    """
    result = {}
    for item in list_of_dicts:
        for key, value in item.items():
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key]] + [value]
            else:
                result[key] = value

    return result


print(mysum('adv', 'sdsd'))
print(mysum([1, 2, 3], [4, 5, 6]))
print(mysum())
print(my_sum_bigger_than('afc', 'adv', 'sdsd', 'edfred', 'aa'))
print(my_sum_bigger_than(10, 5, 20, 30, 6))
print(my_sum_bigger_than('e'))
print(sum_numeric(10, 20, 'a', '30', 'bcd'))
print(join_dicts([{"a": 1, "b": 2, "c": 3}, {"b": 4}, {"c": 6}, {"e": 99}]))
