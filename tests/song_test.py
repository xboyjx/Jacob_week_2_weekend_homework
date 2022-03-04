import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.starlight_song = Song("Starlight")

    def test_song_has_name(self):
        self.assertEqual("Starlight", self.starlight_song.name)