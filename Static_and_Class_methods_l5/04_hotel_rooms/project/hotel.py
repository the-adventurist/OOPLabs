from typing import Type, TypeVar, List


from project.room import Room

T = TypeVar("T", bound="Hotel")


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0
    
    @property
    def guests(self):
        return self.__guests

    @guests.setter
    def guests(self, value):
        self.__guests = sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls: Type[T], stars_count: int) -> T:
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        this_room = [r for r in self.rooms if r.number == room_number][0]
        this_room.take_room(people)
        self.guests += people

    def free_room(self, room_number: int) -> None:
        this_room = [r for r in self.rooms if r.number == room_number][0]
        guest_count = this_room.guests
        this_room.free_room()

    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]
        res = f"Hotel {self.name} has {self.guests} total guests\n"
        res += f"Free rooms: {', '.join(str(r.number) for r in free_rooms)}\n"
        res += f"Taken rooms: {', '.join(str(r.number) for r in taken_rooms)}\n"

        return res
