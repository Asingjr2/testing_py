"""Testing functions on python class.

Additional information in docs: https://docs.python.org/3.6/library/unittest.html#organizing-tests.
"""
import unittest
from unittest import TestCase
from basic_class import Human


# Testing for class property existence
class HumanTestCase(TestCase):
    """Testing human class attributes and functions."""
    def setUp(self):
        print("setting up")
        self.joe = Human("Joe", "28", "male")

    def tearDown(self):
        print("tearing down")

    def test_human(self):
        print("running main test")
        self.assertIsNotNone(self.joe.name)
        self.assertIsNotNone(self.joe.age)
        self.assertIsNotNone(self.joe.gender)
        self.assertIsNotNone(self.joe.bio)
        # Below check even handles spaces!!!
        self.assertEqual(self.joe.bio, "My name is {} and I am {}.".format(self.joe.name, self.joe.age))



# Below allows file to be tested directly like running through -m
if __name__ == "__main__":
    unittest.main()
