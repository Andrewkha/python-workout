#!/usr/bin/env python3

"""Solution to chapter 6, exercise 25: myxml"""


def myxml(tagname, content='', **kwargs):
    """Takes a tag name (string), an optional content string,
    and optional kwargs.

    Returns a string in which "tagname" is an XML tag at the start and end,
    "content" is placed in the middle of the tags, and
    the key-value pairs of kwargs are inserted as attributes in the opening tag.
    """
    params = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f"<{tagname}{params}>{content}</{tagname}>"


def copyfile(input_file, *args):
    """
    Write a copyfile function that takes one mandatory argument—the name of
    an input file—and any number of additional arguments: the names of files to
    which the input should be copied. Calling copyfile('myfile.txt', 'copy1
    .txt', 'copy2.txt', 'copy3.txt') will create three copies of myfile.txt:
    one each in copy1.txt, copy2.txt, and copy3.txt
    """
    with open(input_file) as file:
        text = file.read()

    for out_file in args:
        with open(out_file, 'w') as file_out:
            file_out.write(text)


def mult_ints(*args):
    """
    Write a “factorial” function that takes any number of numeric arguments and
    returns the result of multiplying them all by one another.
    """
    if args:
        result = 1
        for one in args:
            result *= one

        return result


def anyjoin(sequence, glue=' '):
    """
    Write an anyjoin function that works similarly to str.join, except that the first
    argument is a sequence of any types (not just of strings), and the second argument is the “glue”
    that we put between elements, defaulting to " " (a space). So
    anyjoin([1,2,3]) will return 1 2 3, and anyjoin('abc', pass:'**') will return pass:a**b**c
    """

    return glue.join(str(x) for x in sequence)


# print(myxml('foo', 'bar', a=1, b=2, c=3))
# print(myxml('foo', 'bar'))
# print(myxml('foo'))
# copyfile('shoe-data.txt', '1.txt', '2.txt', '3.txt')
# print(mult_ints(1, 2, 4, 5, 67))
print(anyjoin('abc', '**'))
