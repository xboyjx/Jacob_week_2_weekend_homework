import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.starlight_song = Song("Starlight", 200)

    def test_song_has_name(self):
        self.assertEqual("Starlight", self.starlight_song.name)

    def test_song_has_duration(self):
        self.assertEqual(200, self.starlight_song.duration)