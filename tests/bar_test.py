import unittest

from src.song import Song
from src.bar import Bar
from src.room import Room
from src.person import Person

class TestBar(unittest.TestCase):

#setup the test data
    def setUp(self):
        self.song1 = Song("Take me to the river","Talking Heads")
        self.song2 = Song("Black", "Pearl Jam")
        self.song3 = Song("Smooth Criminal", "Michael Jackson")
        self.room1 = Room(1, 12, 5)
        self.room2 = Room(2, 9, 6)
        self.room3 = Room(3, 1, 7)
        self.person1 = Person("Matt", 30, self.song1)
        self.person2 = Person("Alan", 100, self.song2)
        self.person3 = Person("Skint", 1, self.song2)
        self.person4 = Person("Joe", 6, self.song3)
        self.bar = Bar(5)

    def test_selling_drink(self):
        self.assertEqual("Cha-ching", self.bar.drink_sell(self.person2, self.room1))
        self.bar.drink_sell(self.person2, self.room1)
        self.bar.drink_sell(self.person1, self.room1)
        self.assertEqual(15, self.room1.tab)
        self.assertEqual(25, self.person1.wallet)
        self.assertEqual(90, self.person2.wallet)
    
    def test_refusing_drink_when_no_money(self):
        self.assertEqual("You're skint mate", self.bar.drink_sell(self.person3, self.room1))
