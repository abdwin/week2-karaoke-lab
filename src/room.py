
class Room:
    def __init__(self, number, capacity, entry_fee):
        self.number = number
        self.capacity = capacity
        self.entry_fee = entry_fee
        # Why can't we initialize a song list and guest list above in brackets?
        self.songs = []
        self.guests = []
        self.tab = 0

    # Checkin People Method -> Guests - use Person Class
    def checkin_guest(self, person, room):
        if room.capacity > len(self.guests):
            if room.entry_fee <= person.wallet:
                self.guests.append(person.name)
                room.tab += room.entry_fee
                person.wallet -= room.entry_fee
                return "They got in"
            else:
                return "You can't afford this"
        else:
            return "No more room"

    # Checkout Guests Method -> People - use Person Class
    def checkout_guest(self, person):
        self.guests.remove(person.name)

    # Checkout All Guests Method -> People - use Person Class
    def checkout_all_guests(self):
        self.guests.clear()

    # Checkin Song Method into Room 
    def checkin_song(self, song):
        self.songs.append(song)

    # Checkout Song Method from room
    def checkout_song(self, song):
        self.guests.remove(song)

    # Checkout All Songs Method from room
    def checkout_all_songs(self):
        self.guests.clear()

    # Does a Guest have their favourite song on the Songs List - if so "Whooo"
    def check_fav_song(self, person, room):
        for song in self.songs:
            if song.title == person.favsong.title:
                return "Wooohoooooo, yeaaaahhhhh mannnnnnn"
        return "Crap music guys"





    