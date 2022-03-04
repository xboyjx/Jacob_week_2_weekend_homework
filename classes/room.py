class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def add_guest(self, new_guest):
        self.guest_list.append(new_guest)