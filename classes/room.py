class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def add_guest(self, new_guest):
        self.guest_list.append(new_guest)

    def remove_guest(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)