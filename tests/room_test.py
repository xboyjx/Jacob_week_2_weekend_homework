import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.main_room = Room("Main Room")

    def test_room_has_name(self):
        self.assertEqual("Main Room", self.main_room.name)

    def test_room_has_guest_list(self):
        self.assertEqual(0, len(self.main_room.guest_list))

    def test_room_has_song_list(self):
        self.assertEqual(0, len(self.main_room.song_list))
