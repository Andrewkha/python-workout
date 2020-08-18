#!/usr/bin/env python3
"""Solution to chapter 4, exercise 15: rainfall"""


def get_rainfall():
    """Ask the user repeatedly for a city name and mm of rainfall.

    If the city is blank, then stop asking questions,
    and report all cities and rainfall.

    Otherwise, ask for rainfall and add the current rainfall
    to any previous report for that city.
    """

    rainfalls = {}

    while True:
        city = input("Please provide a city name: ").strip()
        if not city:
            break
        rain = int(input("How much rain was there? "))
        rainfalls[city] = rainfalls.get(city, 0) + rain

    for city, rain in rainfalls.items():
        print(f'{city}: {rain}')


def avg_rainfall():
    """
    Instead of printing just the total rainfall for each city, print the total rainfall and
    the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40
    for Boston, you would see that the total was 90 and the average was 30.
    """
    rainfalls = {}

    while True:
        city = input("Please provide a city name: ").strip()
        if not city:
            break
        rain = int(input("How much rain was there? "))
        rainfalls[city] = rainfalls.get(city, []) + [rain]
        print(rainfalls)

    for city, rain in rainfalls.items():
        print(f'{city}: {sum(rain) / len(rain)}')


def text_word_frequency():
    """
    Read through a text file on disk. Use a dict to track how many words of each
    length are in the file—that is, how many three-letter words, four-letter words,
    five-letter words, and so on. Display your results.
    """
    frequency = {}

    with open('../files/61105-0.txt', encoding='utf-8') as file:
        text = file.read()

    for word in text.split():
        length = len(word)
        frequency[length] = frequency.get(length, 0) + 1

    return frequency


# get_rainfall()
# avg_rainfall()
print(text_word_frequency())
