import unittest
from datetime import date
from models.hotel import Hotel
from models.room import Room
from models.guest import Guest
from models.reservation import Reservation

class TestHotel(unittest.TestCase):
    """Testy jednostkowe dla klasy Hotel - sprawdzają poprawność dodawania pokoi, filtrowania ich,
        dokonywania rezerwacji oraz weryfikacji dostępności."""

    def setUp(self):
        """Tworzy obiekt hotelu z dwoma pokojami i jednym gościem do wykorzystania w testach."""
        self.hotel = Hotel("Hotel Testowy", "ul. Przykładowa 1")
        self.room1 = Room("101", "single", 150.0, 1)
        self.room2 = Room("102", "double", 200.0, 2)
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)
        self.guest = Guest("Jan", "Kowalski", "jan@example.com", "123456789")

    def test_add_room_duplicate(self):
        """Test sprawdzający, czy ponowna próba dodania tego samego pokoju powoduje błąd ValueError."""
        with self.assertRaises(ValueError):
            self.hotel.add_room(self.room1)

    def test_find_room_by_number(self):
        """Test sprawdzający poprawność wyszukiwania pokoju po numerze."""
        found = self.hotel.find_room_by_number("101")
        self.assertEqual(found, self.room1)

    def test_get_all_rooms(self):
        """Test sprawdzający, czy hotel zwraca wszystkie dodane pokoje."""
        self.assertEqual(len(self.hotel.get_all_rooms()), 2)

    def test_filter_rooms_by_type(self):
        """Test filtrowania pokoi po typie (np. single, double)."""
        result = self.hotel.filter_rooms(room_type="double")
        self.assertEqual(result, [self.room2])

    def test_filter_rooms_by_capacity(self):
        """Test filtrowania pokoi po maksymalnej pojemności (ilości gości)."""
        result = self.hotel.filter_rooms(capacity=2)
        self.assertEqual(result, [self.room2])

    def test_make_reservation_successful(self):
        """Test sprawdzający poprawność tworzenia nowej rezerwacji."""
        check_in = date(2025, 6, 20)
        check_out = date(2025, 6, 22)
        reservation = self.hotel.make_reservation(self.guest, "101", check_in, check_out)
        self.assertIsInstance(reservation, Reservation)
        self.assertEqual(len(self.hotel.get_all_reservations()), 1)

    def test_make_reservation_conflict(self):
        """Test weryfikujący czy próba rezerwacji pokoju na już zajęty termin zwróci błąd ValueError."""
        check_in = date(2025, 6, 20)
        check_out = date(2025, 6, 22)
        self.hotel.make_reservation(self.guest, "101", check_in, check_out)
        with self.assertRaises(ValueError):
            self.hotel.make_reservation(self.guest, "101", date(2025, 6, 21), date(2025, 6, 23))

    def test_is_room_available_true(self):
        """Test sprawdzający, czy pokój jest dostępny w przypadku braku konfliktu terminów."""
        available = self.hotel.is_room_available(self.room1, date(2025, 7, 1), date(2025, 7, 5))
        self.assertTrue(available)

    def test_is_room_available_false(self):
        """Test sprawdzający, czy pokój zostaje oznaczony jako niedostępny przy konflikcie rezerwacji."""
        self.hotel.make_reservation(self.guest, "101", date(2025, 6, 20), date(2025, 6, 22))
        available = self.hotel.is_room_available(self.room1, date(2025, 6, 21), date(2025, 6, 23))
        self.assertFalse(available)

if __name__ == "__main__":
    unittest.main()

