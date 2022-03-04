import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.main_room = Room("Main Room")
        self.new_guest_1 = Guest ("Jacob")
        self.starlight_song = Song("Starlight", 200)

    def test_room_has_name(self):
        self.assertEqual("Main Room", self.main_room.name)

    def test_room_has_guest_list(self):
        self.assertEqual(0, len(self.main_room.guest_list))

    def test_room_has_song_list(self):
        self.assertEqual(0, len(self.main_room.song_list))

    def test_room_can_add_guest(self):
        self.main_room.add_guest(self.new_guest_1)
        self.assertEqual(1, len(self.main_room.guest_list))

    def test_room_can_remove_guest(self):
        self.main_room.add_guest(self.new_guest_1)
        self.assertEqual(1, len(self.main_room.guest_list))
        self.main_room.remove_guest(self.new_guest_1)
        self.assertEqual(0, len(self.main_room.guest_list))

    def test_room_can_add_song(self):
        self.main_room.add_song(self.starlight_song)
        self.assertEqual(1, len(self.main_room.song_list))
