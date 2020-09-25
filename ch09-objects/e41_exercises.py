"""
    Write an Envelope class, with two attributes, weight (a float, measuring grams)
    and was_sent (a Boolean, defaulting to False).
    There should be three methods:
    (1) send, which sends the letter, and changes was_sent to True, but only
    after the envelope has enough postage;
    (2) add_postage, which adds postage equal to its argument; and
    (3) postage_needed, which indicates how much postage the envelope needs total.
    The postage needed will be the weight of the envelope times 10.
    Now write a BigEnvelope class that works just like Envelope
    except that the postage is 15 times the weight, rather than 10
"""


class Envelope:
    """Envelope class"""

    def __init__(self, weight, sent=False):
        self.weight = weight
        self.sent = sent
        self.postage = 0

    def send(self):
        """Sends the mail"""
        if self.postage >= self.postage_needed():
            self.sent = True

    def add_postage(self, value):
        """adds the postage"""
        self.postage += value

    def postage_needed(self):
        """calculates required postage"""
        return self.weight * 10


class BigEnvelope(Envelope):
    """Big Envelope class"""

    def postage_needed(self):
        return self.weight * 15


class Phone:
    """"
    Create a Phone class that represents a mobile phone. (Are there still nonmobile
    phones?) The phone should implement a dial method that dials a phone number (or simulates doing so).
    Implement a SmartPhone subclass that uses the Phone.dial method but implements
    its own run_app method.
    Now implement an iPhone subclass that implements not only a run_app method, but also its
    own dial method, which invokes the parent’s dial method but whose output is all in lowercase
    as a sign of its coolness
    """

    def dial(self, number):
        """Dial the number"""
        return str(number)


class SmartPhone(Phone):
    """SmartPhone class"""

    def run_app(self, application):
        """Launch application"""
        return f"{application} is run"


class iPhone(SmartPhone):
    """SmartPhone Class"""

    def dial(self, number):
        return super().dial(number).lower()


class Bread:
    """
    Define a Bread class representing a loaf of bread. We should be able to invoke a
    get_nutrition method on the object, passing an integer representing the
    number of slices we want to eat. In return, we’ll receive a dict whose key-value
    pairs will represent calories, carbohydrates, sodium, sugar, and fat, indicating
    the nutritional statistics for that number of slices. Now implement two new
    classes that inherit from Bread, namely WholeWheatBread and RyeBread. Each
    class should implement the same get_nutrition method, but with different
    nutritional information where appropriate.
    """

    nutrition_per_slice = {
        'calories': 10,
        'carbohydrates': 5,
        'sodium': 3,
        'sugar': 20,
        'fat': 30
    }

    def get_nutrition(self, slices):
        """get nutrition per slice"""
        return {category: value * slices for category, value in self.nutrition_per_slice}


class Wheatbread(Bread):
    """White bread"""

    nutrition_per_slice = {
        'calories': 30,
        'carbohydrates': 15,
        'sodium': 13,
        'sugar': 220,
        'fat': 320
    }


p1 = Phone()
print(p1.dial('ksSDSWdkw9293'))
p2 = iPhone()
print(p2.dial('adsfFSDSDafs34q4'))
