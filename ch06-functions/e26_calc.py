#!/usr/bin/env python3

"""Solution to chapter 6, exercise 26: calc"""

import operator


def calc(to_solve):
    """This function expects to get a string containing a
    two-argument math expression in prefix notation, and with
    whitespace separating the operator and numbers.
    The return value is the result from invoking this operation.
    """

    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    operation, first, second = to_solve.split(maxsplit=2)
    first = int(first)
    second = int(second)

    return operations[operation](first, second)


def calc_extended(to_solve):
    """
    Expand the program you wrote, such that the user’s input can contain any
    number of numbers, not just two. The program will thus handle + 3 5 7 or / 100
    5 5, and will apply the operator from left to right—giving the answers 15 and 4,
    respectively
    """
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    operation, *operands = to_solve.split()
    result = int(operands[0])

    for operand in operands[1::]:
        result = operations[operation](result, int(operand))

    return result


def apply_to_each(function, sequence):
    """
    Write a function, apply_to_each, that takes two arguments: a function that takes
    a single argument, and an iterable. Return a list whose values are the result of
    applying the function to each element in the iterable. (If this sounds familiar, it
    might be—this is an implementation of the classic map function, still available in
    Python. You can find a description of map in chapter 7.)
    """
    return [function(x) for x in sequence]


def transform_lines(function, input_file, output_file):
    """
    Write a function, transform_lines, that takes three arguments: a function that
    takes a single argument, the name of an input file, and the name of an output
    file. Calling the function will run the function on each line of the input file,
    with the results written to the output file. (Hint: the previous exercise and this
    one are closely related.)
    """
    with open(input_file) as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write(function(line))


# print(calc('/ 14 7'))
# print(calc_extended('+ 3 5 7'))
# print(apply_to_each(lambda x: x * 3, (5, 3, 4, 6, 7, 8)))
transform_lines(str.upper, 'shoe-data.txt', 'shoe-data-capital.txt')
