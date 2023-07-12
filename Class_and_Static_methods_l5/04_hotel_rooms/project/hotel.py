from typing import List, Type, TypeVar
from project.room import Room

T = TypeVar("T", bound="Hotel")


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> T:
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        this_room = [r for r in self.rooms if r.number == room_number]
        if this_room:
            this_room = this_room[0]
            if this_room.capacity >= people and not this_room.is_taken:
                this_room.guests += people
                this_room.is_taken = True
                self.guests += people

    def free_room(self, room_number: int) -> None:
        this_room = [r for r in self.rooms if r.number == room_number]
        if this_room:
            this_room = this_room[0]
            if this_room.is_taken:
                this_room.is_taken = False
                self.guests -= this_room.guests
                this_room.guests = 0

    def status(self) -> str:
        free_rooms = [r for r in self.rooms if r.guests == 0]
        taken_rooms = [r for r in self.rooms if r.guests > 0]
        res = f"Hotel {self.name} has {self.guests} total guests\n"
        res += f"Free rooms: {', '.join(str(free_room.number) for free_room in free_rooms)}\n"
        res += f"Taken rooms: {', '.join(str(taken_room.number) for taken_room in taken_rooms)}\n"

        return res
