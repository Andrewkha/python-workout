#!/usr/bin/env python3
"""Solution to chapter 1, exercise 3: run_timing"""


def run_timing():
    """Asks the user repeatedly for numeric input.
Prints the average time and number of runs.
"""
    runs = []

    while True:
        run = input("Enter 10 km run time: ")
        if not run:
            break
        runs.append(float(run))

    print(f"Average of {sum(runs) / len(runs)}, over {len(runs)} runs")


def before_and_after(dec: float, before: int, after: int) -> float:
    full, part = str(dec).split('.')
    full = full[-before:]
    part = part[0:after]
    return float(f"{full}.{part}")

# run_timing()
print(before_and_after(1234.5678, 2, 3))


from decimal import Decimal

def decim():
    a = Decimal(input('Enter a: '))
    b = Decimal(input('Enter b: '))
    return a + b


print(decim())
