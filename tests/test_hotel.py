import unittest
from datetime import date
from models.hotel import Hotel
from models.room import Room
from models.guest import Guest
from models.reservation import Reservation

class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Hotel Testowy", "ul. Przykładowa 1")
        self.room1 = Room("101", "single", 150.0, 1)
        self.room2 = Room("102", "double", 200.0, 2)
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)
        self.guest = Guest("Jan", "Kowalski", "jan@example.com", "123456789")

    def test_add_room_duplicate(self):
        with self.assertRaises(ValueError):
            self.hotel.add_room(self.room1)

    def test_find_room_by_number(self):
        found = self.hotel.find_room_by_number("101")
        self.assertEqual(found, self.room1)

    def test_get_all_rooms(self):
        self.assertEqual(len(self.hotel.get_all_rooms()), 2)

    def test_filter_rooms_by_type(self):
        result = self.hotel.filter_rooms(room_type="double")
        self.assertEqual(result, [self.room2])

    def test_filter_rooms_by_capacity(self):
        result = self.hotel.filter_rooms(capacity=2)
        self.assertEqual(result, [self.room2])

    def test_make_reservation_successful(self):
        check_in = date(2025, 6, 20)
        check_out = date(2025, 6, 22)
        reservation = self.hotel.make_reservation(self.guest, "101", check_in, check_out)
        self.assertIsInstance(reservation, Reservation)
        self.assertEqual(len(self.hotel.get_all_reservations()), 1)

    def test_make_reservation_conflict(self):
        check_in = date(2025, 6, 20)
        check_out = date(2025, 6, 22)
        self.hotel.make_reservation(self.guest, "101", check_in, check_out)
        with self.assertRaises(ValueError):
            self.hotel.make_reservation(self.guest, "101", date(2025, 6, 21), date(2025, 6, 23))

    def test_is_room_available_true(self):
        available = self.hotel.is_room_available(self.room1, date(2025, 7, 1), date(2025, 7, 5))
        self.assertTrue(available)

    def test_is_room_available_false(self):
        self.hotel.make_reservation(self.guest, "101", date(2025, 6, 20), date(2025, 6, 22))
        available = self.hotel.is_room_available(self.room1, date(2025, 6, 21), date(2025, 6, 23))
        self.assertFalse(available)

if __name__ == "__main__":
    unittest.main()
