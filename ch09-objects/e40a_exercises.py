"""
Define a Person class, and a population class attribute that increases each time
you create a new instance of Person. Double-check that after you’ve created five
instances, named p1 through p5, Person.population and p1.population are
both equal to 5.
"""


class Person:
    """
    Python provides a __del__ method that’s executed when an object is garbage
    collected. (In my experience, deleting a variable or assigning it to another
    object triggers the calling of __del__ pretty quickly.) Modify your Person class
    such that when a Person instance is deleted, the population count decrements
    by 1. If you aren’t sure what garbage collection is, or how it works in Python, take a
    look at this article: http://mng.bz/nP2a.
    """
    population = 0

    def __init__(self):
        Person.population += 1

    def __del__(self):
        Person.population -= 1


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()

p5 = 10

print(p1.population)
print(Person.population)


class Transaction:
    """
    Define a Transaction class, in which each instance represents either a deposit or a
    withdrawal from a bank account. When creating a new instance of Transaction,
    you’ll need to specify an amount—positive for a deposit and negative for a withdrawal.
    Use a class attribute to keep track of the current balance, which should
    be equal to the sum of the amounts in all instances created to date.
    """
    account = 0

    def __init__(self, amount):
        Transaction.account += amount


transaction1 = Transaction(50)
transaction2 = Transaction(-5)
transaction3 = Transaction(55)

print(Transaction.account)

