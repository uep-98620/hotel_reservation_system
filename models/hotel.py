from typing import List, Optional, Dict
from datetime import date

from .room import Room
from .guest import Guest
from .reservation import Reservation


class Hotel:
    """Reprezentuje hotel i zarządza pokojami oraz rezerwacjami."""

    def __init__(self, name: str, address: str):
        if not name or not isinstance(name, str):
            raise ValueError("Nazwa hotelu musi zawierać conajniej 1 znak.")
        if not address or not isinstance(address, str):
            raise ValueError("Adres hotelu musi zawierać conajniej 1 znak.")

        self.name: str = name
        self.address: str = address
        self.rooms: Dict[str, Room] = {}
        self.reservations: List[Reservation] = []

    def add_room(self, room: Room) -> None:
        """Dodaje pokój do hotelu."""
        if not isinstance(room, Room):
            raise TypeError("Można dodać tylko obiekty klasy Room.")
        if room.number in self.rooms:
            raise ValueError(f"Pokój o numerze {room.number} już istnieje.")
        self.rooms[room.number] = room

    def find_room_by_number(self, number: str) -> Optional[Room]:
        """Zwraca pokój o podanym numerze (jeśli istnieje)."""
        return self.rooms.get(number)

    def get_all_rooms(self) -> List[Room]:
        """Zwraca listę wszystkich pokoi w hotelu."""
        return list(self.rooms.values())

    def filter_rooms(self, room_type: Optional[str] = None, capacity: Optional[int] = None) -> List[Room]:
        """Filtruje pokoje po typie i/lub pojemności."""
        filtered = list(self.rooms.values())

        if room_type:
            filtered = [r for r in filtered if r.room_type.lower() == room_type.lower()]

        if capacity:
            filtered = [r for r in filtered if r.capacity >= capacity]

        return filtered

    def is_room_available(self, room: Room, check_in: date, check_out: date) -> bool:
        """Sprawdza, czy pokój jest dostępny w danym zakresie dat."""
        for reservation in self.reservations:
            if reservation.room == room:
                if check_in < reservation.check_out and check_out > reservation.check_in:
                    return False
        return True

    def make_reservation(self, guest: Guest, room_number: str, check_in: date, check_out: date) -> Reservation:
        """Tworzy rezerwację, jeśli pokój jest dostępny w podanym zakresie dat."""
        room = self.rooms.get(room_number)
        if not room:
            raise ValueError(f"Pokój {room_number} nie istnieje.")
        if not self.is_room_available(room, check_in, check_out):
            raise ValueError(f"Pokój {room_number} jest już zarezerwowany w tym terminie.")

        reservation = Reservation(guest, room, check_in, check_out)
        self.reservations.append(reservation)
        return reservation

    def get_all_reservations(self) -> List[Reservation]:
        """Zwraca listę wszystkich rezerwacji w hotelu."""
        return self.reservations

    def __str__(self) -> str:
        return f"Hotel: {self.name} ({self.address}) - {len(self.rooms)} pokoi."

    def __repr__(self) -> str:
        return f"Hotel(name='{self.name}', address='{self.address}')"
