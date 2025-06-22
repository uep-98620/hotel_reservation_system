from datetime import date
from typing import List, Optional, Dict, Any

from models.guest import Guest
from models.room import Room
from models.hotel import Hotel
from models.reservation import Reservation
from models.payment import Payment

class HotelService:
    """Logika aplikacyjna zarządzająca hotelem, rezerwacjami i płatnościami."""

    def __init__(self, name: str, address: str):
        """Tworzy instancję hotelu."""
        self.hotel = Hotel(name, address)

    def add_room(self, number: str, room_type: str, price_per_night: float, capacity: int) -> Room:
        """Dodaje pokój do hotelu."""
        room = Room(number, room_type, price_per_night, capacity)
        self.hotel.add_room(room)
        return room

    def register_guest(self, first_name: str, last_name: str, email: str, phone_number: str) -> Guest:
        """Rejestruje nowego gościa."""
        return Guest(first_name, last_name, email, phone_number)

    def make_reservation(
        self, guest: Guest, room_number: str, check_in: date, check_out: date
    ) -> Reservation:
        """Tworzy rezerwację, jeśli pokój jest dostępny."""
        return self.hotel.make_reservation(guest, room_number, check_in, check_out)

    def create_payment(self, reservation: Reservation, method: str) -> Payment:
        """Tworzy płatność za rezerwację."""
        return Payment(reservation, method)

    def confirm_payment(self, payment: Payment) -> None:
        """Potwierdza płatność."""
        payment.confirm_payment()

    def list_rooms(self, room_type: Optional[str] = None, capacity: Optional[int] = None) -> List[Room]:
        """Zwraca dostępne pokoje, z możliwością filtrowania."""
        return self.hotel.filter_rooms(room_type, capacity)

    def check_availability(self, room_number: str, check_in: date, check_out: date) -> bool:
        """Sprawdza, czy dany pokój jest dostępny w podanym terminie."""
        room = self.hotel.find_room_by_number(room_number)
        if not room:
            raise ValueError(f"Pokój {room_number} nie istnieje.")
        return self.hotel.is_room_available(room, check_in, check_out)

    def get_all_reservations(self) -> List[Reservation]:
        """Zwraca listę wszystkich rezerwacji w hotelu."""
        return self.hotel.get_all_reservations()

    def simulate_full_booking_flow(self) -> Dict[str, Any]:
        """Symuluje pełny proces rezerwacji i płatności – do testów integracyjnych."""
        # Dodanie pokoi
        room1 = self.add_room("101", "double", 320.0, 2)
        room2 = self.add_room("102", "single", 200.0, 1)

        # Rejestracja gościa
        guest = self.register_guest("Jan", "Nowak", "jan.nowak@example.com", "123456789")

        # Tworzenie rezerwacji
        check_in = date(2025, 7, 10)
        check_out = date(2025, 7, 13)
        reservation = self.make_reservation(guest, "101", check_in, check_out)

        # Tworzenie i potwierdzenie płatności
        payment = self.create_payment(reservation, "karta")
        self.confirm_payment(payment)

        return {
            "guest": guest,
            "room": room1,
            "reservation": reservation,
            "payment": payment
        }
