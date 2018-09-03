"""Program to handle basic testing with proper structure."""
import unittest
from unittest import TestCase


def write(quote):
    print("Nice quote by {}".format(quote.author))


class Quote(object):
    def __init__(self, saying, author, topic):
        self.saying = saying 
        self.author = author
        self.topic = topic

    @property
    def description(self):
        return "{} once said {}".format(self.author, self.saying)


class QuoteTestCase(TestCase):
    """Testing quote class attributes and method.  
    
    Structure requires formal setup and teardown.
    """

    def setUp(self):
        """Occurs before every test is run.  Printing to demonstrate."""
        print("setting up")
        self.words = Quote("Falcon Punch!!!", "Capt. Falcon", "Melee")
    
    def tearDown(self):
        """Occurs after every test is run.  Printing to demonstrate."""
        print("tearing down")

    def test_quote(self):
        print("performing main tests")
        self.assertIsNotNone(self.words.saying)
        self.assertIsNotNone(self.words.author)
        self.assertEqual(self.words.description, "{} once said {}".format(self.words.author, self.words.saying))


# Below allows file to be tested directly like running through python -m my_file.py
if __name__ == "__main__":
    unittest.main()
