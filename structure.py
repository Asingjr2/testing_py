"""Program to handle basic testing with proper structure.

Structure matches docs with new setup and teardown used for each test...shown through print statements.
Factory boy does testing using built in python build, save, and delete functions.
"""
import unittest
from unittest import TestCase


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
    Can also use classmethods that run once before any tests and once when all are done
    """

    @classmethod
    def setUpClass(cls):
        """Printing to show that code happens only once at test process start."""
        print("setUp class")
    
    @classmethod
    def tearDownClass(cls):
        """Printing to show that code happens only once at test process end."""
        print("tearDown class")

    def setUp(self):
        """Occurs before every test is run.  Printing to demonstrate."""
        print("setting up")
        self.words = Quote("Falcon Punch!!!", "Capt. Falcon", "Melee")
    
    def tearDown(self):
        """Occurs after every test is run.  Printing to demonstrate."""
        print("tearing down")

    def test_quote(self):
        print("performing main test 1")
        self.assertIsNotNone(self.words.saying)
        self.assertIsNotNone(self.words.author)

    def test_quote2(self):
        print("performing main test 2")
        self.assertEqual(self.words.description, "{} once said {}".format(self.words.author, self.words.saying))


# Below allows file to be tested directly like running through python -m my_file.py
if __name__ == "__main__":
    unittest.main()
