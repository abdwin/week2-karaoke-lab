import unittest

from src.room import Room
from src.person import Person
from src.song import Song
from src.bar import Bar

class TestRoom(unittest.TestCase):

    #setup the test data for the room object (created by Room class)
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
 
    def test_returns_a_room_num(self):
        self.assertEqual(1, self.room1.number)
        self.assertEqual(2, self.room2.number)
    
    def test_returns_a_room_capacity(self):
        self.assertEqual(12, self.room1.capacity)
        self.assertEqual(9, self.room2.capacity)

    def test_returns_a_room_entry_fee(self):
        self.assertEqual(5, self.room1.entry_fee)
        self.assertEqual(6, self.room2.entry_fee)

    def test_a_room_has_guests(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.assertEqual(2, len(self.room1.guests))

    def test_room_checkout_guests(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.room1.checkout_guest(self.person1, self.room1)
        self.room1.checkout_guest(self.person2, self.room1)
        self.assertEqual(0, len(self.room1.guests))

    def test_room_checkout_guests(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.room1.checkout_all_guests()
        self.assertEqual(0, len(self.room1.guests))

    def test_add_songs_to_room(self):
        self.room1.checkin_song(self.song1)
        self.room1.checkin_song(self.song2)
        self.assertEqual(2, len(self.room1.songs))
        # self.assertEqual(self.room1.songs(0))

    def test_room_capacity(self):
        self.room3.checkin_guest(self.person1, self.room3)
        self.assertEqual('No more room', self.room3.checkin_guest(self.person2, self.room3))
    
    def test_person_has_money_to_pay(self):
        self.room2.checkin_guest(self.person1, self.room2)
        self.assertEqual(1, len(self.room2.guests))
        self.assertEqual("You can't afford this", self.room2.checkin_guest(self.person3, self.room2))
    
    def test_favsong_is_in_room_songlist(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.room1.checkin_guest(self.person3, self.room1)
        self.room1.checkin_guest(self.person4, self.room1)
        self.room1.checkin_song(self.song1)
        self.room1.checkin_song(self.song2)
        self.assertEqual(2, len(self.room1.songs))
        self.assertEqual("Wooohoooooo, yeaaaahhhhh mannnnnnn", self.room1.check_fav_song(self.person2, self.room1))
        self.assertEqual("Crap music guys", self.room1.check_fav_song(self.person4, self.room1))

    def test_spending_of_guests_on_room(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.room1.checkin_guest(self.person3, self.room2)
        self.room1.checkin_guest(self.person4, self.room2)
        self.assertEqual(10, self.room1.tab)

    def test_spending_of_guests_on_room_and_buying_at_bar(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.bar.drink_sell(self.person1, self.room1)
        self.bar.drink_sell(self.person2, self.room1)
        self.bar.drink_sell(self.person2, self.room1)
        self.bar.drink_sell(self.person2, self.room1)
        self.assertEqual(30, self.room1.tab)
   
    def test_spending_of_guests_on_room_and_buying_at_bar_when_no_money(self):
        self.room1.checkin_guest(self.person1, self.room1)
        self.room1.checkin_guest(self.person2, self.room1)
        self.room1.checkin_guest(self.person3, self.room1)
        self.bar.drink_sell(self.person1, self.room1)
        self.bar.drink_sell(self.person2, self.room1)
        self.bar.drink_sell(self.person2, self.room1)
        self.bar.drink_sell(self.person3, self.room1)
        self.assertEqual(25, self.room1.tab) 

