import unittest
from datetime import date, datetime
from models.payment import Payment
from models.reservation import Reservation
from models.guest import Guest
from models.room import Room


class TestPayment(unittest.TestCase):
    """Test dla klasy Payment - weryfikuje poprawność tworzenia płatności oraz działania metod klasy."""

    def setUp(self):
        """Przygotowanie danych testowych - utworzenie gościa, pokoju i rezerwacji."""
        self.guest = Guest("Jan", "Kowalski", "jan@email.com", "123456789")
        self.room = Room("101", "single", 200.0, 1)
        self.reservation = Reservation(self.guest, self.room, date(2025, 7, 1), date(2025, 7, 3))

    def test_create_payment_card(self):
        """Test poprawności utworzenia płatności kartą."""
        payment = Payment(self.reservation, "karta")

        self.assertIsInstance(payment.payment_id, str)
        self.assertEqual(payment.method, "karta")
        self.assertEqual(payment.amount, 400.0)  # 2 noce × 200 zł
        self.assertFalse(payment.paid)
        self.assertIsNone(payment.payment_date)

    def test_create_payment_cash(self):
        """Test poprawności utworzenia płatności gotówką."""
        payment = Payment(self.reservation, "gotówka")

        self.assertEqual(payment.method, "gotówka")
        self.assertEqual(payment.amount, 400.0)
        self.assertFalse(payment.paid)

    def test_invalid_reservation(self):
        """Weryfikacja czy program zwróci błąd TypeError, gdy rezerwacja nie jest obiektem klasy Reservation."""
        with self.assertRaises(TypeError):
            Payment("nie_rezerwacja", "karta")

    def test_invalid_payment_method(self):
        """Weryfikacja czy program zwróci błąd ValueError, gdy metoda płatności nie jest 'karta' lub 'gotówka'."""
        with self.assertRaises(ValueError):
            Payment(self.reservation, "bitcoin")

        with self.assertRaises(ValueError):
            Payment(self.reservation, "uśmiech bąbelka")

    def test_confirm_payment(self):
        """Test działania metody confirm_payment - czy oznacza płatność jako zapłaconą."""
        payment = Payment(self.reservation, "karta")

        # Przed potwierdzeniem
        self.assertFalse(payment.paid)
        self.assertIsNone(payment.payment_date)

        # Potwierdzenie
        payment.confirm_payment()

        # Po potwierdzeniu
        self.assertTrue(payment.paid)
        self.assertIsInstance(payment.payment_date, datetime)

    def test_confirm_payment_twice(self):
        """Weryfikacja czy program zwróci błąd ValueError przy próbie ponownego potwierdzenia płatności."""
        payment = Payment(self.reservation, "gotówka")
        payment.confirm_payment()

        with self.assertRaises(ValueError):
            payment.confirm_payment()

    def test_is_paid(self):
        """Test działania metody is_paid - czy poprawnie zwraca status płatności."""
        payment = Payment(self.reservation, "karta")

        # Przed zapłatą
        self.assertFalse(payment.is_paid())

        # Po zapłacie
        payment.confirm_payment()
        self.assertTrue(payment.is_paid())

    def test_get_summary(self):
        """Test działania metody get_summary - czy zwraca poprawne podsumowanie płatności."""
        payment = Payment(self.reservation, "gotówka")
        summary = payment.get_summary()

        self.assertEqual(summary["payment_id"], payment.payment_id)
        self.assertEqual(summary["reservation_id"], self.reservation.reservation_id)
        self.assertEqual(summary["guest_name"], "Jan Kowalski")
        self.assertEqual(summary["amount"], 400.0)
        self.assertEqual(summary["method"], "gotówka")
        self.assertFalse(summary["paid"])
        self.assertIsNone(summary["payment_date"])

        # Po zapłacie
        payment.confirm_payment()
        summary_paid = payment.get_summary()
        self.assertTrue(summary_paid["paid"])
        self.assertIsNotNone(summary_paid["payment_date"])

    def test_str_representation(self):
        """Weryfikacja czy po wyświetleniu płatności widać jej status."""
        payment = Payment(self.reservation, "karta")

        # Nieopłacona
        self.assertIn("oczekuje na płatność", str(payment))
        self.assertIn("karta", str(payment))

        # Opłacona
        payment.confirm_payment()
        self.assertIn("opłacona", str(payment))

    def test_repr(self):
        """Weryfikacja czy techniczny opis obiektu zawiera pożądane informacje o płatności."""
        payment = Payment(self.reservation, "gotówka")
        rep = repr(payment)

        self.assertIn("Płatność(payment_id=", rep)
        self.assertIn("amount=400.0", rep)
        self.assertIn("method='gotówka'", rep)
        self.assertIn("paid=False", rep)

    def test_different_reservation_amounts(self):
        """Test czy payment poprawnie pobiera kwotę z różnych rezerwacji."""
        # Dłuższa rezerwacja
        long_reservation = Reservation(self.guest, self.room, date(2025, 7, 1), date(2025, 7, 10))
        payment = Payment(long_reservation, "karta")

        self.assertEqual(payment.amount, 1800.0)  # 9 nocy × 200 zł

        # Droższa rezerwacja
        expensive_room = Room("201", "suite", 500.0, 2)
        expensive_reservation = Reservation(self.guest, expensive_room, date(2025, 7, 1), date(2025, 7, 3))
        payment2 = Payment(expensive_reservation, "gotówka")

        self.assertEqual(payment2.amount, 1000.0)  # 2 noce × 500 zł


if __name__ == "__main__":
    unittest.main()