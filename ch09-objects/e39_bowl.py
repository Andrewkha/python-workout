#!/usr/bin/env python3
from e38_scoop import Scoop

"""Solution to chapter 9, exercise 39: bowl"""


class Bowl:
    """Class representing a bowl of ice cream.

The "scoops" attribute is a list, containing scoops.
You can add one or more scoops with the "add_scoops" method.
"""
    def __init__(self):
        self.scoops = []


    def add_scoops(self, *scoops):
        """
        adding scoops into the bowl
        """
        for one in scoops:
            self.scoops.append(one)


    def __repr__(self):
        return ', '.join(x.flavour for x in self.scoops)


# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')
# b = Bowl()
# b.add_scoops(s1, s2)
# b.add_scoops(s3)
# print(b)


class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class TooWideException(Exception):
    pass


class Shelf:
    def __init__(self, width):
        self.books = []
        self.width = width


    def add_book(self, book: Book):
        curr_width = sum(x.width for x in self.books)
        if book.width + curr_width <= self.width:
            self.books.append(book)
        else:
            raise TooWideException


    def has_book(self, title):
        return bool([x for x in self.books if x.title == title])

    def total_price(self):
        return sum(book.price for book in self.books)


b1 = Book('ssd', 'wesd', 23, 1)
b2 = Book('ssd', 'wesd', 2, 6)

shelf = Shelf(5)
shelf.add_book(b1)
shelf.add_book(b2)
print(shelf.total_price())

print(shelf.has_book('ssd'))
print(shelf.has_book('wed'))

