from datetime import date
from typing import Dict, Any
import uuid

from .guest import Guest
from .room import Room

class Reservation:
    """Reprezentuje rezerwację zrobioną przez gościa hotelu dla konkretnego pokoju i terminu.

    Atrybuty:
        reservation_id (str): Unikalny identyfikator rezerwacji.
        guest (Guest): Gość hotelu dokonujący rezerwacji.
        room (Room): Pokój, który został zarezerwowany.
        check_in (date): Data zameldowania.
        check_out (date): Data wymeldowania.
    """

    def __init__(self, guest: Guest, room: Room, check_in: date, check_out: date):
        """Tworzy obiekt rezerwacji."""
        if not isinstance(guest, Guest):
            raise TypeError("Gość musi być obiektem klasy Guest.")
        if not isinstance(room, Room):
            raise TypeError("Pokój musi być obiektem klasy Room.")
        if not isinstance(check_in, date) or not isinstance(check_out, date):
            raise TypeError("Daty zameldowania i wymeldowania muszą mieć format daty.")
        if check_in >= check_out:
            raise ValueError("Data wymeldowania musi być późniejsza niż data zameldowania.")

        self.reservation_id: str = str(uuid.uuid4())
        self.guest: Guest = guest
        self.room: Room = room
        self.check_in: date = check_in
        self.check_out: date = check_out

    def get_duration(self) -> int:
        """Zwraca liczbę nocy pobytu."""
        return (self.check_out - self.check_in).days

    def get_total_price(self) -> float:
        """Oblicza całkowity koszt pobytu."""
        return self.get_duration() * self.room.price_per_night

    def get_summary(self) -> Dict[str, Any]:
        """Zwraca podsumowanie rezerwacji w formie słownika."""
        return {
            "reservation_id": self.reservation_id,
            "guest_name": self.guest.get_full_name(),
            "room_number": self.room.number,
            "check_in": self.check_in.isoformat(),
            "check_out": self.check_out.isoformat(),
            "nights": self.get_duration(),
            "total_price": self.get_total_price(),
        }

    def __str__(self) -> str:
        return (f"Rezerwacja {self.reservation_id}: {self.guest.get_full_name()} - "
                f"Pokój {self.room.number} od {self.check_in} do {self.check_out}")

    def __repr__(self) -> str:
        return (f"Rezerwacja(reservation_id='{self.reservation_id}', "
                f"gość={repr(self.guest)}, pokój={repr(self.room)}, "
                f"zameldowanie={self.check_in}, wymeldowanie={self.check_out})")