import unittest
from datetime import date
from models.guest import Guest
from models.room import Room
from models.reservation import Reservation

class ReservationTest(unittest.TestCase):
    """Testy jednostkowe dla klasy Reservation."""

    def setUp(self):
        """Tworzy obiekty Guest i Room do wykorzystania w testach."""
        self.guest = Guest("Jan", "Kowalski", "jan@example.com", "987654321")
        self.room = Room("101", "double", 250.0, 2)
        self.check_in = date(2025, 7, 1)
        self.check_out = date(2025, 7, 5)

    def test_create_reservation(self):
        """Test poprawnego utworzenia rezerwacji."""
        reservation = Reservation(self.guest, self.room, self.check_in, self.check_out)
        self.assertIsInstance(reservation.reservation_id, str)
        self.assertEqual(reservation.guest, self.guest)
        self.assertEqual(reservation.room, self.room)
        self.assertEqual(reservation.check_in, self.check_in)
        self.assertEqual(reservation.check_out, self.check_out)

    def test_get_duration(self):
        """Test poprawnego obliczenia liczby nocy."""
        reservation = Reservation(self.guest, self.room, self.check_in, self.check_out)
        self.assertEqual(reservation.get_duration(), 4)

    def test_get_total_price(self):
        """Test obliczenia całkowitego kosztu pobytu."""
        reservation = Reservation(self.guest, self.room, self.check_in, self.check_out)
        self.assertEqual(reservation.get_total_price(), 1000.0)

    def test_get_summary(self):
        """Test poprawności danych zwracanych przez get_summary."""
        reservation = Reservation(self.guest, self.room, self.check_in, self.check_out)
        summary = reservation.get_summary()
        self.assertEqual(summary["guest_name"], "Jan Kowalski")
        self.assertEqual(summary["room_number"], "101")
        self.assertEqual(summary["check_in"], "2025-07-01")
        self.assertEqual(summary["check_out"], "2025-07-05")
        self.assertEqual(summary["nights"], 4)
        self.assertEqual(summary["total_price"], 1000.0)

    def test_invalid_guest_type(self):
        """Test zgłoszenia błędu, gdy gość nie jest instancją klasy Guest."""
        with self.assertRaises(TypeError):
            Reservation("NieGość", self.room, self.check_in, self.check_out)

    def test_invalid_room_type(self):
        """Test zgłoszenia błędu, gdy pokój nie jest instancją klasy Room."""
        with self.assertRaises(TypeError):
            Reservation(self.guest, "NiePokój", self.check_in, self.check_out)

    def test_invalid_date_type(self):
        """Test zgłoszenia błędu, gdy daty są w złym formacie."""
        with self.assertRaises(TypeError):
            Reservation(self.guest, self.room, "2025-07-01", "2025-07-05")

    def test_checkout_before_checkin(self):
        """Test zgłoszenia błędu, gdy data wymeldowania jest wcześniejsza niż zameldowania."""
        with self.assertRaises(ValueError):
            Reservation(self.guest, self.room, date(2025, 7, 5), date(2025, 7, 1))

    def test_str_representation(self):
        """Test czy metoda __str__ zawiera kluczowe informacje."""
        reservation = Reservation(self.guest, self.room, self.check_in, self.check_out)
        self.assertIn("Jan Kowalski", str(reservation))
        self.assertIn("101", str(reservation))

    def test_repr_representation(self):
        """Test czy metoda __repr__ zawiera kluczowe dane techniczne."""
        reservation = Reservation(self.guest, self.room, self.check_in, self.check_out)
        rep = repr(reservation)
        self.assertIn("reservation_id", rep)
        self.assertIn("zameldowanie=2025-07-01", rep)
        self.assertIn("wymeldowanie=2025-07-05", rep)

if __name__ == "__main__":
    unittest.main()