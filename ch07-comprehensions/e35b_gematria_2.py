#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35b: gematria_equal_words"""

from e35a_gematria_1 import gematria_dict

GEMATRIA = gematria_dict()


def gematria_for(word):
    """Function that calculates the gematria
    for a given word, an argument passed as a string.
    """
    return sum(GEMATRIA.get(letter, 0) for letter in word)


def gematria_equal_words(input_word):
    """Function that takes a string (word) as input,
    and returns a list of strings (words) whose calculated
    gematria is identical.
    """
    gem = gematria_for(input_word)
    with open('words.txt') as file:
        return [word.strip() for word in file if gematria_for(word) == gem]


def temperature():
    """
    Create a dict whose keys are city names, and whose values are temperatures in
    Fahrenheit. Now use a dict comprehension to transform this dict into a new
    one, keeping the old keys but turning the values into the temperature in
    degrees Celsius.
    """
    cities = {'NN': 100, 'Moscow': 80, 'St Pete': 60, 'Riga': 75}

    def far_to_cel(t_far):
        return (t_far - 32) * 5 / 9

    return {city: far_to_cel(temp) for city, temp in cities.items()}


def books_transform():
    """
    Create a list of tuples in which each tuple contains three elements:
    (1) the author’s first and last names,
    (2) the book’s title, and
    (3) the book’s price in U.S. dollars.
    Use a dict comprehension to turn this into a dict whose keys are
    the book’s titles, with the values being another (sub-) dict, with keys for (a) the
    author’s first name, (b) the author’s last name, and (c) the book’s price in
    U.S. dollars.
    """

    books = {('Daniel Defoe', 'Robinson Cruso', 100),
             ('Alexander Pushkin', 'Eugene Onegin', 110),
             ('Alex Tolstoy', 'Anna Karenina', 5)}

    return {book[1]: {'fname': book[0].split()[0],
                      'lname': book[0].split()[1],
                      'price': book[2]} for book in books}


def currency_convert(currency_name):
    """
    Create a dict whose keys are currency names and whose values are the price of
    that currency in U.S. dollars. Write a function that asks the user what currency
    they use, then returns the dict from the previous exercise as before, but with its
    prices converted into the requested currency.
    """
    currencies = {'RUR': 75, 'EUR': 0.8, 'KRN': 15, 'NIS': 5}

    books = books_transform()
    return {title: {'fname': details['fname'],
                    'lname': details['lname'],
                    'price': details['price'] * currencies.get(currency_name)}
            for title, details in books.items()}


print(temperature())
# print(gematria_for('aa'))
# print(gematria_for('kukushka'))
# print(gematria_for('Zygobranchia'))
# print(gematria_equal_words('kukushka'))
print(currency_convert('RUR'))
