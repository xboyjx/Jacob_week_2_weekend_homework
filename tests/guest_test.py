import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jacob")

    def test_guest_has_name(self):
        self.assertEqual("Jacob", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet_balance)
        