class Room:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.guest_list = []
        self.song_list = []

    def add_guest(self, new_guest):
        if len(self.guest_list) < self.max_capacity:
            self.guest_list.append(new_guest)
        else:
            return "Room has reached max capacity"

    def remove_guest(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)

    def add_song(self, song_to_add):
        self.song_list.append(song_to_add)