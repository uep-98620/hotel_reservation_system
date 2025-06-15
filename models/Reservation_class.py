from datetime import date
from typing import Dict, Any
import uuid

from .guest import Guest
from .room import Room

class Reservation:
    """Reprezentuje rezerwację dokonaną przez gościa hotelu.

    Atrybuty:
        reservation_id (str): Unikalny identyfikator rezerwacji.
        guest (Guest): Gość hotelu dokonujący rezerwacji.
        room (Room): Pokój, który został zarezerwowany.
        check_in (date): Data zameldowania.
        check_out (date): Data wymeldowania.
    """

    def __init__(self, guest: Guest, room: Room, check_in: date, check_out: date):
        """Inicjalizuje obiekt klasy Reservation.
        Args:
            guest: Guest: Gość hotelu.
            room: Room: Pokój hotelowy.
            check_in: date: Data zameldowania.
            check_out: date: Data wymeldowania.

        Raises:
            TypeError: Jeśli gość nie jest prawidłowym obiektem klasy Guest np. nie istnieje gość o danym imieniu i nazwisku,
            TypeError: Jeśli pokój nie jest prawidłowym obiektem klasy Room np. podano pokój numer 101, gdy hotel posiada pokoje do numeru 100,
            TypeError: Jeśli data została podana w nieprawidłowym formacie np. check_in = date(2025, 7, 23), zamiast check_in= „2025-07-23”,
            ValueError: Jeśli data wymeldowania jest wcześniejsza niż zameldowania np. check_in = date(2025-07-23), check_out = date(2025-07-21).
        Dzięki temu program nie przyjmie niepoprawnych danych i nie stworzy błędnej rezerwacji.
        Po sprawdzeniu poprawności danych, program tworzy nowy obiekt rezerwacji, zgodnie z zadeklarowanymi atrybutami, i przypisuje mu dane.
        """
        if not isinstance(guest, Guest):
            raise TypeError("Podany gość nie istnieje. Gość musi należeć do klasy Guest.")
        if not isinstance(room, Room):
            raise TypeError("Podany pokój nie istnieje. Pokój musi należeć do klasy Room.")
        if not isinstance(check_in, date) or not isinstance(check_out, date):
            raise TypeError("Data zameldowania i wymeldowania muszą mieć format daty (RRR-MM-DD).")
        if check_in >= check_out:
            raise ValueError("Data wymeldowania musi być późniejsza niż data zameldowania.")

        self.reservation_id: str = str(uuid.uuid4())
        self.guest: Guest = guest
        self.room: Room = room
        self.check_in: date = check_in
        self.check_out: date = check_out

    def get_duration(self) -> int:
        """Oblicza i zwraca liczbę nocy w ramach danej rezerwacji,
        Returns:
            int: różnica między datą zameldowania, a datą wymeldowania, z której wyciągnięto liczbę pełnych dni jako liczbę całkowitą. """
        return (self.check_out - self.check_in).days

    def get_total_price(self) -> float:
        """Oblicza całkowity koszt pobytu w hotelu
        Returns:
            float: iloczyn w formie zmiennoprzecinkowej, obliczonej liczby nocy (get_duration) i ceny jednej nocy w danym pokoju (price_per_night) będącą atrybutem klasy Room
         """
        return self.get_duration() * self.room.price_per_night

    def get_summary(self) -> Dict[str, Any]:
        """Returns:
            Reservation_id – unikalny identyfikator rezerwacji
            Guest_name – metoda z klasy Guest, która zwraca imię i nazwisko gościa
            Room_number – unikalny numer pokoju, atrybut klasy Room
            Check_in – data zameldowania w formacie ISO (RRR-MM-DD)
            Check_out - data wymeldowania w formacie ISO (RRR-MM-DD)
            Nights – liczba nocy obliczona za pomocą get_duration()
            Total_price – całkowity koszt pobytu w hotelu obliczony za pomocą get_total_price()
"""
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
                (f"Rezerwacja {self.reservation_id}: {self.guest.get_full_name()} - "
                f"Pokój {self.room.number} od {self.check_in} do {self.check_out}")

    def __repr__(self) -> str:
        return (f"Rezerwacja(reservation_id='{self.reservation_id}', "
                f"gość={repr(self.guest)}, pokój={repr(self.room)}, "
                f"zameldowanie={self.check_in}, wymeldowanie={self.check_out})")