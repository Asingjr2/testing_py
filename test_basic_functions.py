"""Practice with basic testing functionality.

Run testing in cmd line with python -m unittest test_file.py.
Can run directly with __main reference below. 
"""
import unittest
from unittest import TestCase
from basic_class import Human
from basic_functions import (
    add,
    minus,
    multi,
    divide, 
    floor_divide,
    mod
    )


# Basic testing class
class TestBasicFunctions(TestCase):
    def test_add(self):
        self.assertEqual(add(10,5), 15)
        self.assertEqual(add(-5,5), 0)
        self.assertEqual(add(-10,0), -10)

    def test_minus(self):
        self.assertEqual(minus(10,5), 5)
        self.assertEqual(minus(-5,5), -10)
        self.assertEqual(minus(-10,0), -10)

    
    def test_multi(self):
        self.assertEqual(multi(10,5), 50)
        self.assertEqual(multi(-5,5), -25)
        self.assertEqual(multi(-10,0), 0)

    def test_divide(self):
        self.assertEqual(divide(10,5), 2)
        self.assertEqual(divide(-9,3), -3)
        self.assertEqual(divide(-10,4), -2.5)

    def test_floor_divide(self):
        """Using floor divide to round initial result down."""
        self.assertEqual(floor_divide(10,5), 2)
        self.assertEqual(floor_divide(-9,3), -3)
        self.assertEqual(floor_divide(5, 2), 2)

    def test_mod(self):
        self.assertEqual(mod(10,5), 0)
        self.assertEqual(mod(7,2), 1)
        self.assertEqual(mod(6,2), 0)


# Testing for class property existence
class HumanTestCase(TestCase):
    def test_human(self):
        joe = Human("Joe", "28", "male")

        self.assertIsNotNone(joe.name)
        self.assertIsNotNone(joe.age)
        self.assertIsNotNone(joe.gender)



# Below allows file to be tested directly like running through -m
if __name__ == "__main__":
    unittest.main()
