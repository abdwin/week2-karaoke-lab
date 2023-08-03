import unittest

from src.fizz_buzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_returns_a_number(self):
        self.assertEqual(4, fizzbuzz(4))

    def test_returns__fizz_when_passed_a_multiple_of_3(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_returns__buzz_when_passed_a_multiple_of_5(self):
        self.assertEqual("buzz", fizzbuzz(5))

    def test_returns__fizzbuzz_when_passed_a_multiple_of_3_and_5(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))
    