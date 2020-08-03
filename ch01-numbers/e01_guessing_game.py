#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1: Guessing game"""
import random


def guessing_game():
    number = random.randint(1, 100)
    print(number)
    guess = int(input("Provide your guess: "))

    while guess != number:
        if guess > number:
            print("Too high")
        else:
            print("Too low")
        guess = int(input("Provide your guess: "))

    print("Just right")


"""Just 3 chances"""


def guessing_game_tree():
    number = random.randint(1, 100)
    print(number)

    for step in range(0, 3):
        guess = int(input("Provide your guess: "))

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("Just right")
            break

    else:
        print("Too many attempts")


# guessing_game()
guessing_game_tree()