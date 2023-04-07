class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        return self.rooms.append(room)

    def take_room(self, room_number, people):
        the_room = [r for r in self.rooms if r.number == room_number][0]
        return the_room.take_room(people)

    def free_room(self, room_number):
        the_room = [r for r in self.rooms if r.number == room_number][0]
        return the_room.free_room()

    def status(self):
        self.guests = sum(r.guests for r in self.rooms)
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(free_rooms)}\n" \
                 f"Taken rooms: {', '.join(taken_rooms)}"
        return result


